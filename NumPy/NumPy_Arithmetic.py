import numpy as np

listA = [[1, 3, 6]]
listB = [[4, 2, 1]]
arrayA = np.array(listA)
arrayB = np.array(listB)
addArray = arrayA + arrayB
multiplyArray = arrayA * arrayB

"""Addition"""
print("Addition of Arrays: %s" % addArray)

"""Multiplication"""
print("Multiplication of Arrays: %s" % multiplyArray)