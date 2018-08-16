
import pandas

fileName = "pima-indians-diabetes.data.csv"
rawData = open(fileName, "rt")
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = pandas.read_csv(rawData, names=colNames)
pandas.set_option("display.width", 100)
pandas.set_option("precision", 3)
pandas.set_option('display.max_columns', 9)
descriptiveStatistics = data.describe()
print(descriptiveStatistics)