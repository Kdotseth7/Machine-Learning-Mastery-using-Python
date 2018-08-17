# Correlation Matrix Plot
import pandas
import matplotlib.pyplot as plt

fileName = "pima-indians-diabetes.data.csv"
rawData = open(fileName, "rt")
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = pandas.read_csv(rawData, names=colNames)
correlationData = data.corr()

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlationData, vmin=-1, vmax=1)
fig.colorbar(cax)
plt.show()