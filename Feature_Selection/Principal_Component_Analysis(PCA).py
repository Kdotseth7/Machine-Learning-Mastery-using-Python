from pandas import read_csv
from sklearn.decomposition import PCA
import numpy

fileName = "pima-indians-diabetes.data.csv"
rawData = open(fileName, "rt")
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = read_csv(rawData, names=colNames)
array = data.values
X = array[:, :-1]
Y = array[:, -1]
pca = PCA(n_components=3)
fit = pca.fit(X, Y)
features = fit.transform(X)
numpy.set_printoptions(precision=3)
print("Explained Variance Ratio : %s" % fit.explained_variance_ratio_)
print("--------------------------------------------------------------------------------")
print("Components :")
print(fit.components_)
print("--------------------------------------------------------------------------------")
print("Top 5 rows of Selected Features:")
print(features[0:5, :])