#!/usr/bin/env python
# -- coding: utf-8 --
"""
主成分分析（Principal Component Analysis），是一种用于探索高维数据的技术。
PCA通常用于高维数据集的探索与可视化。还可以用于数据压缩，数据预处理等。
PCA可以把可能具有线性相关性的高维变量合成为线性无关的低维变量，称为主成分（principal components），
新的低维数据集会尽可能的保留原始数据的变量，可以将高维数据集映射到低维空间的同时，尽可能的保留更多变量。

注意：降维就意味着信息的丢失，这一点一定要明确，如果用原始数据在模型上没有效果，
期望通过降维来进行改善这是不现实的，不过鉴于实际数据本身常常存在的相关性，
我们可以想办法在降维的同时将信息的损失尽量降低。当你在原数据上跑了一个比较好的结果，
又嫌它太慢模型太复杂时候才可以采取PCA降维。
"""
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
Y = iris.target
X_bar = np.mean(X, axis=0)
print(iris['feature_names'])
print(X_bar)

cov_mat = np.cov(X.T)
eig_val, eig_vec = np.linalg.eig(cov_mat)
eig_pairs = zip(eig_val, eig_vec)
top3_components = sorted(eig_pairs, reverse=True)[:3]
W = np.array([components[1] for components in top3_components]).reshape(-1, 3)
res = np.dot(X, W)
fig = plt.figure()
ax = Axes3D(fig)
ax.set_title('Iris Dataset by PCA', size=14)
ax.scatter(res[:, 0], res[:, 1], res[:, 2], c=Y)
ax.set_xlabel('First eigenvector')
ax.set_ylabel('Second eigenvector')
ax.set_zlabel('Third eigenvector')
ax.w_xaxis.set_ticklabels(())
ax.w_yaxis.set_ticklabels(())
ax.w_zaxis.set_ticklabels(())
plt.show()
