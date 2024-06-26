import numpy as np
import cv2


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
    

class FindingNemo:
    def __init__(self, train_image):

        self.light_orange = (1, 190, 200)
        self.dark_orange = (18, 255, 255)
        self.light_white = (0, 0, 200)
        self.dark_white = (145, 60, 255)
        self.light_black = (0, 0, 0)
        self.dark_black = (350,290,180)

        self.knn = KNN(k=3)
        X_train, Y_train = self.convert_image_to_dataset(train_image)
        self.knn.fit(X_train, Y_train)
        
    
    def convert_image_to_dataset(self, image):
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        pixels_list_hsv = image_hsv.reshape(-1, 3)

        mask_orange = cv2.inRange(image_hsv, self.light_orange, self.dark_orange)
        mask_white = cv2.inRange(image_hsv, self.light_white, self.dark_white)
        # mask_black = cv2.inRange(image_hsv, self.light_black, self.dark_black)
        final_mask = mask_orange + mask_white #+ mask_black

        X_train = pixels_list_hsv / 255
        Y_train = final_mask.reshape(-1,) // 255

        return X_train, Y_train

    def remove_background(self, test_image):
        test_image_hsv = cv2.cvtColor(test_image, cv2.COLOR_BGR2HSV)

        X_test = test_image_hsv.reshape(-1, 3) / 255
        Y_pred = self.knn.predict(X_test)

        output = Y_pred.reshape(test_image.shape[:2])
        output = output.astype('uint8')

        final_result = cv2.bitwise_and(test_image, test_image, mask=output)
        return final_result
    

