import numpy

fileName = "pima-indians-diabetes.data.csv"
rawData = open(fileName, "rt")
data = numpy.loadtxt(rawData, delimiter=",")
print(data)
print("-----------------------------------------------------------------")
print("Dimensions of Data:")
print(data.shape)