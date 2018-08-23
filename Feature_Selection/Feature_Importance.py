from pandas import read_csv
from sklearn.ensemble import ExtraTreesClassifier
import numpy
fileName = "pima-indians-diabetes.data.csv"
rawData = open(fileName, "rt")
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = read_csv(rawData, names=colNames)
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
model = ExtraTreesClassifier()
model.fit(X, Y)
# numpy.set_printoptions(precision=3)
print("Feature Importance Values : %s" % model.feature_importances_)