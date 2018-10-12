# Automatic Backward Elimination

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

# Preparing the data for Backward Elimination
X = np.append(np.ones(shape = (50, 1)).astype(int), X, axis = 1) # Convert array of 1's to int

# Building model using Backward Elimination

import statsmodels.formula.api as sm

def backwardElimination(x, sl): # Called Function
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(endog=Y, exog=x).fit()
        maxPVal = max(regressor_OLS.pvalues).astype(float)
        if(maxPVal > sl):
            for j in range(0, numVars-i):
                if(regressor_OLS.pvalues[j].astype(float) == maxPVal):
                    x = np.delete(x, j, 1)
    else: 
        print(regressor_OLS.summary())
    return x

X_opt = X[:, [0, 1, 2, 3, 4, 5]]
SL = 0.05
X_Modeled = backwardElimination(X_opt, SL) # Calling Function