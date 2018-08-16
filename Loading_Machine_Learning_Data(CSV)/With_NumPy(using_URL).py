import numpy
import urllib.request

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
rawData = urllib.request.urlopen(url)
data = numpy.loadtxt(rawData, delimiter=",")
print(data)
print("-----------------------------------------------------------------")
print("Dimensions of Data:")
print(data.shape)