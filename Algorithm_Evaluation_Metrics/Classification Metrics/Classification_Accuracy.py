from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
fileName = "pima-indians-diabetes.data.csv"
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = read_csv(fileName, names=colNames)
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
seed = 7
model = LogisticRegression()
kFold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(model, X, Y, scoring="accuracy", cv=kFold)
print("Classification Accuracy ---->")
print("Ratio : %.3f" % (results.mean()))
print("Mean : %.3f" % (results.mean()*100))
print("Standard Deviation : %.3f" % (results.std()*100))