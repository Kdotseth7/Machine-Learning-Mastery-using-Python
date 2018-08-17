# Correlation Matrix Plot
import pandas
import matplotlib.pyplot as plt
import numpy

fileName = "pima-indians-diabetes.data.csv"
rawData = open(fileName, "rt")
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = pandas.read_csv(rawData, names=colNames)
correlationData = data.corr()

# Customizing the matrix
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlationData, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0, 9, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(colNames)
ax.set_yticklabels(colNames)
plt.show()