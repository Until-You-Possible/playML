# @Time:2022/9/4 10:07
# @Author:Ray
# @File:ToPmml.py.py

import pandas

iris_df = pandas.read_csv("./data/Iris.csv")
iris_X = iris_df[iris_df.columns.difference(["Species"])]
iris_y = iris_df["Species"]

from sklearn.tree import DecisionTreeClassifier
from sklearn2pmml.pipeline import PMMLPipeline

print(iris_df)
