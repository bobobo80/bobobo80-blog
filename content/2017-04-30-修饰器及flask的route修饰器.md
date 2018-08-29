Title: 修饰器及flask的route修饰器
Date: 2017-04-30
Category: flask

python的修饰器是python的一个特色，也是比较难理解的地方，不过运用得当的话会非常优雅和简洁。
通常的两种修饰器形式是无参数的双层结构，即
```python
def decorator(f):
    def wrapper(*args, **kwargs):
        # do some thing before f
        return f(*args, **kwargs)
    return wrapper
```
这样，即定义了一个无参的修饰器，使用时在对应函数的前面加上@decorator即可。
```python
@decorator
def foo():
    # do some thing
    return
```
相当于
```python
foo = decorator(foo)
```
相当于
```python
foo = wrapper
```
这样，当调用foo时，会先运行wrapper中的代码，在进入foo的执行代码。
因为decorator返回的是wrapper函数引用，所以只在foo被调用时，wrapper中的代码采用运行。

而对于需要带额外参数的修饰器，一般是采用三层结构。
```python
def decorator(arg1):
    # do some thing 
    def decorator_func(f):
        def wrapper(*arg, **kwargs):
            # do some thin before f
            return f(*arg, **kwargs)
        return wrapper
    return decorator_func
```
在以函数为参数的外层，再加了一层带其他参数的函数定义。
使用时在对应的函数定义前
```python
@decorator(arg)
def foo():
    # do some thing
    return
```
这样相当于
```python
foo = decorator(arg)(foo)
```
相当于
```python
foo = decorator_func(foo)
```
相当于
```python
foo = wrapper
```
其中decorator的参数可以用于内嵌的deocrator_func和wrapper中
这里需要注意一下各个区间段的运行时间，里层的wrapper中的代码在foo在程序运行时被调用时的之前被运行。而decorator中如果有加入逻辑代码的话，那么将在python解释器读取到函数定义时就被运行。
而flask中的route修饰器就采用了这个用法。
来看一下route的定义，去掉注释。
```python
def route(self, rule, **options):
    def decorator(f):
        endpoint = options.pop("endpoint", f.__name__)
        self.add_url_rule(rule, endpoint, f, **options)
        return f
    return decorator
```
route是带参修饰器，应该是三层结构，不过由于无需wrapper中进行相关操作，所以可以这么定义，相当于wrapper什么也没有。
也就是相当于
```python
def route(self, rule, **options):
    def decorator(f):
        endpoint = option.pop("endpoint", f.__name__)
        self.add_url_rule(rule, endpoint, f, **options)
        def wrapper(**options):
            return f(**options)
        return wrapper
    return decorator
```
来看看route的使用
```python
@route('/', methods=['GET', 'POST'])
def index():
    # do some thing
    return render_template('index.html')
```
这样在解释器初始运行时，读到index和route修饰器时，会运行对应decorator中的代码，即运行add_url_rule()方法，即把路由规则加入到app的map中。而index只会在客户端请求后，路由被匹配后被调用。
所以flask就这样优雅的实现了地址路由的设置。
route修饰器的主要目的是为在在初始运行时就运行相应的add_url_rule()等内容，所以，如果当使用多个文件来设置flask应用时，需要注意包含route的view部分py文件，处于在刚开始被引用或导入，这样才能被解释器运行。以狗书的blueprint结构为例，在app所在包的__init__.py中,定义create_app()方法，其中注册每个blueprint模块，这里会导入各个模块包，所以在每个模块包的__init__.py中，需要引用该模块的view
```python
from . import views
```
这样，就能在create_app()的导入包时，初始化路由设定了。

参考资料
[廖雪峰python教程-修饰器](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000)