"""Series is a 1-D arrays where rows are labelled as time axis"""

import pandas
import numpy

dataList = [1, 2, 3]
myArray = numpy.array(dataList)
rowNames = ["a", "b", "c"]
mySeries = pandas.Series(myArray, index=rowNames)
print(mySeries)
print("-----------------")
print(mySeries[1])  # Accessing elements like Array
print("-----------------")
print(mySeries["a"])  # Accessing elements like dictionary
