import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

class KNN:
    def __init__(self, k):
        self.k = k

    # training
    def fit(self, X, Y):
        self.X_train = X
        self.Y_train = Y

    def euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def predict(self, x_list):
        y_list = []
        for x in x_list:
            distances = []
            for x_train in self.X_train:
                d = self.euclidean_distance(x, x_train)
                distances.append(d)

            nearest_neighbors = np.argsort(distances)[0:self.k]
            result = np.bincount(self.Y_train[nearest_neighbors])
            y = np.argmax(result)
            y_list.append(y)
        return y_list
    
    def evaluate(self, X, Y):
        Y_pred = self.predict(X)
        accuracy = np.sum (Y_pred == Y) / len(Y)
        return accuracy
    

if __name__ == "__main__":
    iris = load_iris()
    X = iris.data
    Y = iris.target

    print(X.shape, Y.shape)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    print(X_train.shape, Y_train.shape)
    print(X_test.shape, Y_test.shape)

    knn_myself = KNN(k=3)
    knn_myself.fit(X_train, Y_train)
    accuracy = knn_myself.evaluate(X_test, Y_test)
    print("Accuracy:", accuracy)


    knn_sklearn = KNeighborsClassifier(n_neighbors=3)
    knn_sklearn.fit(X_train, Y_train)
    accuracy = knn_sklearn.score(X_test, Y_test)
    print("Accuracy:", accuracy)
