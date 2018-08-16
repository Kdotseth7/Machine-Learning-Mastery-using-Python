
"""Peek at your data using head() function"""

import pandas

fileName = "pima-indians-diabetes.data.csv"
rawData = open(fileName, "rt")
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = pandas.read_csv(rawData, names=colNames)
peek = data.head(20)
print("First 20 rows of Data: \n %s" % peek)
