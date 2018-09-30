from pandas import read_csv
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
fileName = "pima-indians-diabetes.data.csv"
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = read_csv(fileName, names=colNames)
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
loocv = LeaveOneOut()
model = LogisticRegression()
results = cross_val_score(model, X, Y, cv=loocv)
print("Accuracy --->")
print("Mean: %.3f%%" % (results.mean()*100.0))
print("Standard Deviation: %.3f%%" % (results.std()*100.0))