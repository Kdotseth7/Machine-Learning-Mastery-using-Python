from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

fileName = "pima-indians-diabetes.data.csv"
rawData = open(fileName, "rt")
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = read_csv(rawData, names=colNames)
array = data.values
X = array[:, :-1]
Y = array[:, -1]
model = LogisticRegression()
rfe = RFE(model, n_features_to_select=3, step=1)
fit = rfe.fit(X, Y)
features = fit.transform(X)
print("No. of features selected: %s" % fit.n_features_)
print("Features selected: %s" % fit.support_)
print("Feature Ranking: %s" % fit.ranking_)
print("Top 5 rows of Selected Features:")
print(features[0:5, :])