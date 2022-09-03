# @Time:2022/8/31 15:50
# @Author:Ray
# @File:testCase.py
import sys


class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def func(a, b, c):
    return a + b + c


if __name__ == '__main__':
    # arr = []
    # for i in range(1, len(sys.argv)):
    #     arr.append((int(sys.argv[i])))
    dog = Test("dog", 12)
    print(dog.age)
