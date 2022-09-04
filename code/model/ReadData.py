# @Time:2022/9/4 01:39
# @Author:Ray
# @File:ReadData.py.py

from sklearn import datasets
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

iris = datasets.load_iris()

X = iris.data[:, :2]
y = iris.target
plt.scatter(X[y == 0, 0], X[y == 0, 1], color="red", marker="o")
plt.scatter(X[y == 1, 0], X[y == 1, 1], color="blue",  marker="*")
plt.scatter(X[y == 2, 0], X[y == 2, 1], color="green", marker="+")
# plt.scatter(X[:, 0], X[:, 1])
plt.show()
print(X.shape)
