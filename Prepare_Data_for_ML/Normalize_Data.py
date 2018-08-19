import pandas
import numpy
import sklearn.preprocessing as skp

fileName = "pima-indians-diabetes.data.csv"
rawData = open(fileName, "rt")
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = pandas.read_csv(rawData, names=colNames)
array = data.values
X = array[:, :-1]
Y = array[:, -1]
normalizer = skp.Normalizer()
rescaledX = normalizer.fit_transform(X)
numpy.set_printoptions(precision=3)
print("Normalized Input Features(first 5 rows & all columns): ")
print("-----------------------------------------------------------")
print(rescaledX[0:5, :])
print("-----------------------------------------------------------")