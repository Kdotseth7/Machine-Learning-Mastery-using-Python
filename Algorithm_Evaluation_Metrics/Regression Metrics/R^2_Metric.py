from pandas import read_csv
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
fileName = "housing.csv"
colNames = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
data = read_csv(fileName, delim_whitespace=True, names=colNames)
array = data.values
X = array[:, 0:13]
Y = array[:, 13]
model = LinearRegression()
seed = 7
kFold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(model, X, Y, cv=kFold, scoring="r2")
print("R^2 (R Squared) ---->")
print("Mean : %.3f" % (results.mean()))
print("Standard Deviation : %.3f" % (results.std()))