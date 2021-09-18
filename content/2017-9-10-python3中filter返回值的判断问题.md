Title: python3中filter返回值的判断问题
Date: 2017-09-10
Category: Tech
Tags: python

最早接触python3来说，最明显的变化就是print方法了，另一个非常大的变化
是返回值生成器类型的使用。

在python2中，很多返回list类型的方法，在python3中都返回生成器对象，
比如最著名的range()，在python3中返回生成器，即python2中的xrange()。
而很多其他方法也是如此，比如list相关的map,reduce,filter方法，
还有dict操作的keys(),items()等，都是由原来的返回list类型，
转而返回生成器类型。

这就需要在使用if判断时注意了，比如filter方法，如果使用if判断，
就需要注意了，比如下面的情况
```python
if filter(lambda x: x>0, [-1,-2]):
    print('if True')
```
在python2中，因为filter返回的是一个空数组[]，if判断将是False。

而在python3中，filter返回为filter对象，if判断将是True，
将执行if中的语句。

不过对于dict的keys等方法，则不是这样，当dict为{}空字典时，
dict.keys()返回的dict_keys对象会根据里面是否有内容而进行对应的判断。
```python
if adict.keys():
    print('dict a is not empty.')
```

