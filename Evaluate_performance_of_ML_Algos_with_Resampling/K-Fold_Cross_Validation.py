from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

fileName = "pima-indians-diabetes.data.csv"
rawData = open(fileName, "rt")
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = read_csv(rawData, names=colNames)
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
kFold = KFold(n_splits=10, random_state=7)
model = LogisticRegression()
results = cross_val_score(model, X, Y, cv=kFold)
print("Accuracy --->")
print("Mean: %.3f%%" % (results.mean()*100.0))
print("Standard Deviation: %.3f%%" % (results.std()*100.0))