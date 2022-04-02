# coding=utf-8
# @Time:2022/3/18 11:10 AM
# @Author:Ray
# @File:LinearRegression.py.py
import numpy as np


# from .metrics import r2_score

class LinearRegression:
    def __init__(self):
        # 系数
        self.coef = None
        # 截距
        self.interception = None
        self._theta = None

    def fit_normal(self, X_train, y_train):
        """
        根据训练数据集x_train y_train训练 Linear Regression模型
        """
        assert X_train.shape[0] == y_train.shape[0], "the size of X_train must be equal to the size of y_train"
        # 关于数据公式转化代码 多翻numpy的doc
        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        self._theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)
        self.interception = self._theta[0]
        self.coef = self._theta[1:]
        return self

    def predict(self, X_predict):
        """ 给定待预测的数据集 X_predict，返回表示X_predict的结果向量 """
        assert self.interception is not None and self.coef is not None, "Must fit before predict"
        assert X_predict.shape[1] == len(self.coef), "the feature number of X_predict must be equal to X_train"
        X_b = np.hstack([np.ones((len(X_predict), 1)), X_predict])
        return X_b.dot(self._theta)

    def score(self, X_test, y_test):
        """ 根据数据集 X_test and y_test 确定当前模型的精准度"""
        y_predict = self.predict(X_test)
        # return r2_score(y_test, y_predict)

    def __repr__(self):
        return "LinearRegression()"
