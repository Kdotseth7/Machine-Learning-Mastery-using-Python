""""List is similar to array and uses Square bracket notation - []"""
pyList = [1, 2, 3, 4]
print("Whole List: %s" % pyList)
print("2nd element: %s" % pyList[2])
print("Appending element 5: ")
pyList.append(5)
print(pyList)
print("Length of List: %d" % len(pyList))
print("Printing List using For-in loop: ")
for value in pyList:
    print(value)