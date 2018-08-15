"""Data Frame is a Multi-Dimensional Array in which rows and columns can be labelled
   Pandas are used for slicing and dicing data """

import pandas
import numpy

mdList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mdArray = numpy.array(mdList)
rName = ["a", "b", "c"]
cName = ["I", "II", "III"]
dataFrame = pandas.DataFrame(mdArray, index=rName, columns=cName)
print(dataFrame)

print("-----------------------")

# Indexing Columns
print("Method 1:")
print("One column (I):\n%s" % dataFrame["I"])
print("Method 2:")
print("One column (II):\n%s" % dataFrame.one)

