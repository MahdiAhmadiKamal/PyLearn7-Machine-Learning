import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from perceptron import Perceptron

#Generating simulated dataset for regression problem:
#The 'make_regression' function generates samples for inputs (features) and output (target) 
#by applying random 'linear regression model'.

x, y, coef = datasets.make_regression(n_samples=200,#number of samples
                                      n_features=1,#number of features
                                      n_informative=1,#number of useful features 
                                      noise=20,#bias and standard deviation of the guassian noise
                                      coef=True,#true coefficient used to generated the data
                                      random_state=0) #set for same data points for each run

#Scale feature x (years of experience) to range 0..20
x = np.interp(x, (x.min(), x.max()), (0, 20))

#Scale target y (salary) to range 20000..150000 
y = np.interp(y, (y.min(), y.max()), (20000, 150000))

# plt.plot(x,y, ".")
# plt.title("Employee's salary")
# plt.xlabel("Experience (year)")
# plt.ylabel("Salary")
# plt.show()

#If we want the data to be presented in pandas dataframe format:
df = pd.DataFrame(data={'experience':x.flatten(),'salary':y})

#Spliting data to train and test datasets:
X = df["experience"].values                         #or: X = np.array(data["Height"])
Y = df["salary"].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("Y_train shape:", Y_train.shape)
print("Y_test shape:", Y_test.shape)

#Fitting model on the employee's salary dataset:
perc = Perceptron(1, 0.0001, 0.01, 10)
perc.fit(X_train, Y_train)