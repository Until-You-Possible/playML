# coding=utf-8
# @Time:2022/2/26 4:04 PM
# @Author:Ray
# @File:SimpleLinearRegression.py

#
import numpy as np


class SimpleLinearRegression1:
    def __init__(self):
        # 初始化 simple linear regression
        self.a_ = None
        self.b_ = None

    def fit(self, x_train, y_train):
        """
        :param x_train: 根据训练数据x_train, y_train训练 simple linear regression模型
        :param y_train:
        :return:

        """
        assert x_train.ndim == 1, \
            "simple linear regression can only solve single feature training data"
        assert len(x_train) == len(y_train), \
            "the size of x_train must be equal to the size of y_train"

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        num = 0.0
        d = 0.0

        for x, y in zip(x_train, y_train):
            num += (x - x_mean) * (y - y_mean)
            d += (x - x_mean) ** 2

        self.a_ = num / d
        self.b_ = y_mean - self.a_ * x_mean

        return self

    def predict(self, x_predict):
        # 给定待预测的数据集x_predict 返回 x_predict的向量结果
        assert x_predict.ndim == 1, "simple linear regressor can only solve single feature training data"
        assert self.a_ is not None and self.b_ is not None, "must fit before predict"

        return np.array([self._predict(x) for x in x_predict])

    def _predict(self, x_single):
        """
        :param x_single:  给定单个待预测的数据x_single。返回x的预测结果
        :return:
        """
        return self.a_ * x_single + self.b_

    def __repr__(self):
        return "SimpleLinearRegression1"

        
