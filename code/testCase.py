# @Time:2022/8/31 15:50
# @Author:Ray
# @File:testCase.py
import sys


def func(a, b, c):
    return a + b + c


if __name__ == '__main__':
    arr = []
    for i in range(1, len(sys.argv)):
        arr.append((int(sys.argv[i])))

    print(func(arr[0], arr[1], arr[2]))
