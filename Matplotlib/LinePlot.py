import matplotlib.pyplot as plt
import numpy

"""Line Plot"""
pyList = [1, 2, 3, 4, 5, 6]
myArray = numpy.array(pyList)
plt.plot(myArray)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()