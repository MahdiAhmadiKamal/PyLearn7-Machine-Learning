import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split


class Perceptron:
    def __init__(self, input_size, lr_w, lr_b, epochs):
        self.w = np.random.rand(input_size)
        self.b = np.random.rand(1, 1)
        self.learning_rate_w = lr_w
        self.learning_rate_b = lr_b
        self.epochs = epochs

    def fit(self, X_train, Y_train):

        X_train = X_train.reshape(-1, 1)
        Y_train = Y_train.reshape(-1, 1)
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.set_figwidth(12)
        losses = []

        for j in range(self.epochs):
            for i in range(X_train.shape[0]):
                x = X_train[i]
                y = Y_train[i]

                y_pred = x * self.w + self.b
                error = y - y_pred

                #SGD update
                self.w = self.w + (error * x * self.learning_rate_w)
                self.b = self.b + (error * self.learning_rate_b)

                #MAE
                loss = np.mean(np.abs(error))
                losses.append(loss)

                Y_pred = X_train * self.w + self.b
                ax1.clear()
                ax1.scatter(X_train, Y_train, color='blue')
                ax1.plot(X_train, Y_pred, color='red')
                ax1.set_title("Employee's salary")
                ax1.set_xlabel("Experience (year)")
                ax1.set_ylabel("Salary")

                ax2.clear()
                ax2.plot(losses)
                ax2.set_title("Loss")
                plt.pause(0.01)

    def predict(self, X_test):
        Y_pred = []
        for x_test in X_test:
            y_pred = x_test @ self.w + self.b
            Y_pred.append(y_pred)
        return np.array(Y_pred)

    def evaluate(self, X_test, Y_test, metric):
        y_pred = self.predict(X_test)
       
        if metric == "mae":
            loss = np.sum(np.abs(Y_test - y_pred)) / len (Y_test)
        elif metric == "mse":
            loss = np.sum((Y_test - y_pred)**2) / len (Y_test)

        return loss