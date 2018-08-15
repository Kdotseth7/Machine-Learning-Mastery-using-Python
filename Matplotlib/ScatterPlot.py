import matplotlib.pyplot as plt
import numpy

"""Scatter Plot"""
xList = [0, 1, 4, 9, 16, 49]
yList = [0, 2, 4, 6, 8, 14]
xArray = numpy.array(xList)
yArray = numpy.array(yList)
plt.scatter(xArray, yArray)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()