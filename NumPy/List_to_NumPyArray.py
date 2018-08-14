import numpy as np

"""1-D Array"""
myList = [1, 2, 3]
myArray = np.array(myList)
print(myArray)
print(myArray.shape)

print("--------------------------")

"""2-D Array"""
myList2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
myArray2 = np.array(myList2)
print(myArray2)
print(myArray2.shape)

print("--------------------------")

"""Access Data"""
print("First Row: %s" % myArray2[0])
print("Last Row: %s" % myArray2[-1])
print("Array Item [1, 2]: %s" % myArray2[1, 2])
print("Whole Column(2nd): %s" % myArray2[:, 2])
print("Whole Row(1st): %s" % myArray2[1, :])