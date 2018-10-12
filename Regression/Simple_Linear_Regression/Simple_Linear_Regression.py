# Simple Linear Regression

# Importing the Libraries
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt

# Importing the Dataset
fileName = "Salary_Data.csv"
data = read_csv(fileName)
array = data.values
X = array[:, :-1]
Y = array[:, 1]

# Splitting the Dataset into Training set and Test set
from sklearn.model_selection import train_test_split
seed = 0
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=seed)

# Feature Scaling(Performed by the Library itself)

# Fitting Simple Linear Regression to Training set
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, Y_train)

# Predicting the Test set Results
Y_pred = model.predict(X_test)

# Visualizing the Training set Results￼
plt.scatter(X_train, Y_train, color="red")
plt.plot(X_train, model.predict(X_train), color="blue")
plt.title("Salary vs Experience(Training Set)")
plt.xlabel("Experience(in yrs)")
plt.ylabel("Salary(in $)")
plt.show()

# Visualizing the Test set Results￼
plt.scatter(X_test, Y_test, color="red")
plt.plot(X_train, model.predict(X_train), color="blue")
plt.title("Salary vs Experience(Test Set)")
plt.xlabel("Experience(in yrs)")
plt.ylabel("Salary(in $)")
plt.show()