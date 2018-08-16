
import pandas

fileName = "pima-indians-diabetes.data.csv"
rawData = open(fileName, "rt")
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = pandas.read_csv(rawData, names=colNames)
print(data)
print("-----------------------------------------------------------------")
print("Dimensions of Data:")
print(data.shape)