# 主成分分析
# 减少系统的维数，保留足以描述个数据点特征的信息
# scikit-learn 库中fit_tranform（）函数就是用来降维的属于PCA对象，使用前先导入PCA模块sklearn.decomposition，然后使用PCA（）构造函数
# 用n_components选项制定要降到几维
# 此外，3D散点图要用到matplotlib的mpl_toolkits.mpplot3d模块。
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()
x = iris.data[:, 1]  # x-axis- petal length
y = iris.data[:, 2]  # y-axis - petal width
species = iris.target  # Species
x_reduced = PCA(n_components=3).fit_transform(iris.data)

# SCATTERPLOT 3D
fig = plt.figure()
ax = Axes3D(fig)
ax.set_title('Iris Dataset by PCA', size=14)
ax.scatter(x_reduced[:, 0], x_reduced[:, 1], x_reduced[:, 2], c=species)
ax.set_xlabel('First eigenvector')
ax.set_ylabel('Second eigenvector')
ax.set_zlabel('Third eigenvector')
ax.w_xaxis.set_ticklabels(())
ax.w_yaxis.set_ticklabels(())
ax.w_zaxis.set_ticklabels(())
plt.show()
