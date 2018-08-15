"""Dictionary is mapping of names to values like key-value pairs. Uses Curly Bracket Notation - {}"""
myDict = {"A": 1, "B": 2, "C": 3}
print("A value: %d" % myDict["A"])
myDict["A"] = 11  # Updating Key Value
print("Keys: %s" % myDict.keys())  # Print the keys
print("Values: %s" % myDict.values())  # Print the values
print("Printing values using For-in loop")
for val in myDict:
    print(myDict[val])