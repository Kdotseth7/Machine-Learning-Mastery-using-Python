# Random Forest Classification

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test) # No need to fit Test Set as its already fitted to Training Set

# Fitting classifier to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = "entropy", random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix(Classification Evaluation Metric)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix : %s " % (cm))

# Visualizing the Training Set Results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
x1Values = np.arange(start = X_set[:, 0].min()-1, stop = X_set[:, 0].max()+1, step = 0.01)
x2Values = np.arange(start = X_set[:, 1].min()-1, stop = X_set[:, 1].max()+1, step = 0.01)
X1, X2 = np.meshgrid(x1Values, x2Values) # numpy.meshgrid(array of x values, array of y values) is used to create a rectangular grid of pixel points
                                          
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green'))) # To draw a contour between the 2 classes seperated as red and green regions
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j) # It draws a scatter plot where red dot corresponds to 0 & green dot corresponds to 1
plt.title('Random Forest Classification (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend() # Legend defines the color for each class label
plt.show()

# Visualizing the Test Set Results
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test
x1Values = np.arange(start = X_set[:, 0].min()-1, stop = X_set[:, 0].max()+1, step = 0.01)
x2Values = np.arange(start = X_set[:, 1].min()-1, stop = X_set[:, 1].max()+1, step = 0.01)
X1, X2 = np.meshgrid(x1Values, x2Values)                                       
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green'))) 
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Random Forest Classification (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend() 
plt.show()