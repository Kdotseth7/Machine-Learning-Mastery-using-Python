# Polynomial Regression

# Importing the Libraries
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt

# Importing the Dataset
fileName = "Position_Salaries.csv"
data = read_csv(fileName)
X = data.iloc[:, 1:2].values # 1:2 to ensure X is always a matrix
Y = data.iloc[:, 2].values # Ensure Y is always a vector

# Splitting Dataset into Training Set and Test Set - No need as Dataset is very small

# Feature Scaling - Performed by the Library itself

# No need for Encoding Categorical Data(Position Column) as Level Column corresponds to a numeric value for the same

# Fitting Polynomial Regression to Dataset --VS-- Fitting Polynomial Regression to Dataset

"""Fitting Linear Regression to Dataset"""

from sklearn.linear_model import LinearRegression
regressor_Linear1 = LinearRegression()
regressor_Linear1.fit(X, Y)

"""Fitting Linear Regression to Dataset"""

from sklearn.preprocessing import PolynomialFeatures
regressor_Poly = PolynomialFeatures(degree = 4)
X_Poly = regressor_Poly.fit_transform(X)
regressor_Linear2 = LinearRegression()
regressor_Linear2.fit(X_Poly, Y)

# Visualizing Linear Regression Results

plt.scatter(X, Y, color = "red")
plt.plot(X, regressor_Linear1.predict(X), color = "blue")
plt.title("Truth or Bluff (Linear Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

# Visualizing Polynomial Regression Results

X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, Y, color = "red")
plt.plot(X_grid, regressor_Linear2.predict(regressor_Poly.fit_transform(X_grid)), color = "blue")
plt.title("Truth or Bluff (Polynomial Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

# Predicting a new Result with Linear Regression

X_linear_pred = regressor_Linear1.predict(X)
print("Predicted Previous Salary of new employee(Linear Regression) : ")
print(regressor_Linear1.predict(6.5))

# Predicting a new Result with Polynomial Regression

X_poly_pred = regressor_Linear2.predict(regressor_Poly.fit_transform(X_grid))
print("Predicted Previous Salary of new employee(Polynomial Regression) : ")
print(regressor_Linear2.predict(regressor_Poly.fit_transform(6.5)))