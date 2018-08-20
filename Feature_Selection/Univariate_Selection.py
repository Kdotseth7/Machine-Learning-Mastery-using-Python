from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

fileName = "pima-indians-diabetes.data.csv"
rawData = open(fileName, "rt")
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = read_csv(rawData, names=colNames)
array = data.values
X = array[:, :-1]
Y = array[:, -1]
test = SelectKBest(score_func=chi2, k=4)  # score_func = Chi_Square Test & k = no. of top features selected
fit = test.fit(X, Y)
set_printoptions(precision=3)
print("Score of each feature : %s" % fit.scores_)
features = fit.transform(X)
print("Top 4 Selected features:")
print(features[0:5, :])