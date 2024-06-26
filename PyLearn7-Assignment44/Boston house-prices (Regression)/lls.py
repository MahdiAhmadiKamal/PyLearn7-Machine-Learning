import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


class LLS:
    def __init__(self):
        ...

    def fit(self, X, Y):
        self.X_train = X
        self.Y_train = Y

    def slope(self, X_train, Y_train):
        return np.matmul(np.matmul(np.linalg.inv(np.matmul(X_train.T, X_train)), X_train.T), Y_train)
    
    def predict(self, x_new_list):
        y_list = []
        for x_new in x_new_list:
            slp = self.slope
            y = slp * x_new
            y_list.append(y)

        return y_list
    
    def evaluate(self, X, Y):
        Y_pred = self.predict(X)
        accuracy = np.sum (Y_pred == Y) / len(Y)
        return accuracy






