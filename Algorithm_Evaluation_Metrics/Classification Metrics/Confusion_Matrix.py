from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
fileName = "pima-indians-diabetes.data.csv"
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = read_csv(fileName, names=colNames)
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
seed = 7
model = LogisticRegression()
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=seed)
model.fit(X_train, Y_train)
predicted = model.predict(X_test)
matrix = confusion_matrix(Y_test, predicted)
print("Confusion Matrix ---->")
print(matrix)
print("Accuracy: %.3f" % (accuracy_score(Y_test, predicted)))
