
import pandas
import matplotlib.pyplot as plt

fileName = "pima-indians-diabetes.data.csv"
rawData = open(fileName, "rt")
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = pandas.read_csv(rawData, names=colNames)
data.plot(kind="box", subplots=True, layout=(3, 3), sharex=False, sharey=False)
plt.show()