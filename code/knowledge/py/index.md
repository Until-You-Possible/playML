### 关于python中的__init__

在py中__init__文件的作用是将一个文件夹编程一个py模块，py中的每个模块包中都有__init__.py的文件

1：在py中 类方法和普通方法的函数又一个特殊的区别---他们必须有一个额外的参数，但是调用这个方法的时候 你不用为这个参数赋值
py会提供这个值。这个特别的变量指的是对象本身。按照惯例他的名称是 self、
参考c++或者java的this


2：py中 循环

```python
list = [6,2,8,3,1]

list = [x**2 for x in mylist]
print(list)
```

```python
# 输出
[36, 4, 64, 9, 1]
```


3:  py中 __repr__(self) 函数

py中 有办法将任意的值转化为字符串，将他传入 str()或者是 repr() 函数

函数 str() 用于将值转化为适用与人阅读的形式
函数 repr() 转化为供解释器读取的形式

repr（）函数 得到的字符串通常可以用来重新获取该对象。repr的输入对python比较友好，通常情况下 obj===eval(repr(obj))这个等式是成立的

```python
obj='I love Python'
obj==eval(repr(obj))
True
```
str()没有这个功能  会报错

repr() 函数
```python
repr([0,1,2,3])
'[0,1,2,3]'
repr('Hello')
"'Hello'"

str(1.0/7.0)
'0.142857142857'
repr(1.0/7.0)
'0.14285714285714285'
```

4: python中的zip方法

zip()函数是py的内置函数之一 他可以将多个序列(列表，元组，集合，字典，字符串，以及range()) "压缩" 成一个zip对象，其实所谓的压缩就是将这些
序列中对应位置的元素重新组合，生成一个新的元组

```python

zip(iterable, ....)
# 其中 iterable。表示多个列表。tuple dict, set str 甚至可以是range()区间

my_list = [11,12,13]
my_tuple = (21,22,23)

print([x for x in zip(my_list,my_tuple)])

my_dic = {31:2,32:4,33:5}
my_set = {41,42,43,44}

print([x for x in zip(my_dic)])

my_pychar = "python"
my_shechar = "shell"

print([x for x in zip(my_pychar,my_shechar)])

```

***__name__***

```text

__name__属性
所有的模块都有一个内置的属性__name__，__name__的值取决于如何使用这个模块
eg: 有一个test.py的模块。包含__name__, 当导入模块时候， __name__都是模块文件名
print(__name__) 会得到 test

但是， 如果将其作为脚本使用，__name__就是一个特殊的值 __main__
eg python test.py
print(__name__) => __main__

总结下： 当模块导入时，模块名称是文件名，而当模块作为脚本独立运行时，名称为__main__

```




