import csv
import numpy

fileName = "pima-indians-diabetes.data.csv"
rawData = open(fileName, "rt")
fileReader = csv.reader(rawData, delimiter=",", quoting=csv.QUOTE_NONE)
x = list(fileReader)
data = numpy.array(x).astype("float")
print(data)

print("-----------------------------------------------------------------")
print("Dimensions of Data:")
print(data.shape)