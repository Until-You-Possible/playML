from sklearn.neighbors import KNeighborsClassifier
import numpy as np

raw_data_X = [[3.393533211, 2.331273381],
              [3.110073483, 1.781539638],
              [1.343808831, 3.368360954],
              [3.582294042, 4.679179110],
              [2.280362439, 2.866990263],
              [7.423436942, 4.696522875],
              [5.745051997, 3.533989803],
              [9.172168622, 2.511101045],
              [7.792783481, 3.424088941],
              [7.939820817, 0.791637231]
              ]
raw_data_y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

X_train = np.array(raw_data_X)
y_train = np.array(raw_data_y)
x = np.array([8.093607318, 3.365731514])
# 创建算法instance
kNN_classifier = KNeighborsClassifier(n_neighbors=6)
# 进行一次fit 拟合我们的训练数据->得到需要的模型
kNN_classifier.fit(X_train, y_train)
# print(kNN_classifier.fit(X_train, y_train))
result = kNN_classifier.predict(x.reshape(1, -1))
print(type(result))
