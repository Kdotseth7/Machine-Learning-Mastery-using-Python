
import pandas
import matplotlib.pyplot as plt

fileName = "pima-indians-diabetes.data.csv"
rawData = open(fileName, "rt")
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = pandas.read_csv(rawData, names=colNames)
data.plot(kind="density", subplots=True, layout=(3, 3), sharex=False)
plt.show()