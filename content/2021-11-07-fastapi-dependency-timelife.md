Title: Fastapi中dependency的生命周期
Date: 2021-11-07
Category: Tech
Tags: fastapi, dependency

## 发现问题

最近使用fastapi时，出现了一个alchemysql数据库连接池的错误。超过了默认的连接池限制。按理说自己的服务只有一个人在用，应该不会出现这种问题。
```
sqlalchemy.exc.TimeoutError: QueuePool limit of size 5 overflow 10 reached, connection timed out, timeout 30.00 (Background on this error at: https://sqlalche.me/e/14/3o7r)
```
联想到最近的修改是增加了一个文件下载接口，所以查到了原因，是这个接口占用了db连接池。

我最开始是用了fastapi作者在fullstack模板里给的[方法](https://github.com/tiangolo/full-stack-fastapi-postgresql/blob/490c554e23343eec0736b06e59b2108fdd057fdc/%7B%7Bcookiecutter.project_slug%7D%7D/backend/app/app/api/deps.py#L46)写的验证用户登陆状态的dependency。比如下面这个接口，调用了Depends(deps.get_current_active_user)，来验证jwt里的用户。
```python
@router.get("/{id}", response_model=schemas.Item)
def read_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get item by ID.
    """
    pass
```
get_current_active_user函数在最里层，使用了get_db，这个函数使用了Generator，在调用时返回db连接，在结束时关闭db连接。
```python
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
```
问题就出在了关闭连接这里。那这个get_db举例，当depends调用get_db时，会调用SessionLocal开启一个db连接和事务，然后直到这个请求返回response后才会调用finally后的close。所以如果一个接口内部不光只有db操作，并且在请求最开始调用了get_db开启了db连接，同时后面还有其他一些时间长的操作(比如读文件，请求其他api等)，那么这个db连接就会被一直占用着，直到这个请求结束才会关闭。同时这还是一个db事务，如果在最开始有写操作或带锁读操作，还会有长时间的db锁。

我在文档里找到了Depends还有个[use_cache用法](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/#using-the-same-dependency-multiple-times)。默认是True，在同一个请求里，如果Depends调用了同一个函数，在第二次调用时会用cache中的值。所以当一个请求里不同的地方调用了get_db，那么会使用同一个session，不会再创建第二个db连接了，就是在同一个连接和同一个事务里。不过如果把use_cache设置为False，那么在不同的地方调用get_db后，会创建新的db连接和事务。但是，当调用get_db后，并不会立刻执行close，仍然是要在整个请求结束后才执行close。

## 可能会引起的问题的情况

Depends的这个问题或特性，可能会在Depends中有一些独立的db请求后，没有及时释放db连接。所以这些情况下引起问题：
- 在请求最开始，通过Depends获取了db session，比如用户验证。但之后，在这个接口中有时间长的操作，长时间占用db连接。
- 在请求最开始，通过Depends获取了db session，比如用户验证，但用户db在一个不同的库，和后面的业务db不在一起。而后面执行的是业务db的操作，导致用户db连接长时间不用，在最后才释放。

## 如何解决

因为Depends的这个用法，那么为了及时释放db连接，就不用Generator的方法了。比如可以单独写一个方法，在函数内部就关闭db连接。这样Depends调用这个函数后，也不会导致db连接占用的问题。不过如果user库和业务库在同一个db,那么就没有必要这样了，这样会导致同一个请求连接两次db。
```python
def get_current_active_user_with_single_session(
    token: str = Depends(reusable_oauth2)
) -> models.User:
    # unpackage jwt ...
    try:
        db = SessionLocal()
        user = crud.user.get(db, id=token_data.sub)
    finally:
        db.close()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/{id}", response_model=schemas.Item)
def read_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user_with_single_session),
) -> Any:
    pass
```