# Multiple Linear Regression using Backward Elimination

# Importing the Libraries
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt

# Importing the Dataset
fileName = "50_Startups.csv"
data = read_csv(fileName)
X = data.iloc[:, :-1].values
Y = data.iloc[:, 4].values

# Encoding Categorical Data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder() # 0, 1, 2 in one column
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features=[3]) # Dummy Variables
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting Dataset into Training Set and Test Set
from sklearn.model_selection import train_test_split
seed = 0
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=seed)

# Feature Scaling(Performed by the Library itself)

# Fitting Simple Linear Regression to Training set
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, Y_train)

# Predicting the Test set Results
Y_pred = model.predict(X_test)

# -----------------------------------------------------------------------------------------------------

# Preparing the data for Backward Elimination
X = np.append(np.ones(shape = (50, 1)).astype(int), X, axis = 1) # Convert array of 1's to int

# Building model using Backward Elimination

import statsmodels.formula.api as sm
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog=Y, exog=X_opt).fit() # OLS is Ordinary Least Square Model
results = regressor_OLS.summary()
print(results)
# Removing the 2nd Dummy Variable Predictor
X_opt = X[:, [0, 1, 3, 4, 5]]
regressor_OLS = sm.OLS(endog=Y, exog=X_opt).fit() 
results = regressor_OLS.summary()
print(results)
# Removing the 1st Dummy Variable Predictor
X_opt = X[:, [0, 3, 4, 5]]
regressor_OLS = sm.OLS(endog=Y, exog=X_opt).fit() 
results = regressor_OLS.summary()
print(results)
# Removing the Administration Predictor
X_opt = X[:, [0, 3, 5]]
regressor_OLS = sm.OLS(endog=Y, exog=X_opt).fit() 
results = regressor_OLS.summary()
print(results)
# Removing the Marketing Spend Predictor
X_opt = X[:, [0, 3]]
regressor_OLS = sm.OLS(endog=Y, exog=X_opt).fit()
results = regressor_OLS.summary()
print(results) 
