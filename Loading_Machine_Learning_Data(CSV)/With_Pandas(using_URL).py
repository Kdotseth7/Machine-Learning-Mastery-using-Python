
import pandas
import urllib.request

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
rawData = urllib.request.urlopen(url)
colNames = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = pandas.read_csv(rawData, names=colNames)
print(data)
print("-----------------------------------------------------------------")
print("Dimensions of Data:")
print(data.shape)