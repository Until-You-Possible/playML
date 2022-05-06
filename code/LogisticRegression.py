# @Time:2022/5/6 11:19
# @Author:Ray
# @File:LogisticRegression.py
import numpy as np


class LogisticRegression:
    def __init__(self):
        # 系数
        self.coef = None
        # 截距
        self.interception = None
        self._theta = None

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
