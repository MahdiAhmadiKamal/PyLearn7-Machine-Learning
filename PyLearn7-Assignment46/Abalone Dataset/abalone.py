import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from perceptron import Perceptron


#Loading data
data = pd.read_csv("abalone.csv")

# plt.scatter(data['Length'], data['Height'], marker='.')
# plt.title("Abalone's length vs abalone's height")
# plt.xlabel('Length')
# plt.ylabel('Height')
# plt.legend(['data'], loc='upper left')
# plt.show()

#Spliting data to train and test datasets:
X = data["Length"].values                         #or: X = np.array(data["Height"])
Y = data["Height"].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.6)

#Fitting model on the abalone dataset:
perc = Perceptron(1, 0.0001, 0.01, 1)
perc.fit(X_train, Y_train)