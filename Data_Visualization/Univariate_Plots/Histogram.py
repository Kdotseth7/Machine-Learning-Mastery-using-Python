"""Histograms are used to group data into bins and provide no. of observations in each bin"""

import pandas
import matplotlib.pyplot as plt

fileName = "pima-indians-diabetes.data.csv"
rawData = open(fileName, "rt")
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = pandas.read_csv(rawData, names=colNames)
data.hist()
plt.show()

# age, pedi & test have an Exponential Distribution
# mass, skin & pres have a Gaussian Distribution
