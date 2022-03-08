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
