import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split


# Load Data
data = pd.read_csv("dataset.csv")
data.fillna(0.0, inplace=True)

X = data.iloc[:, :-1].values        # :-1 means upto last column
Y = data.iloc[:, -1].values         # -1 means last column

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(12 , activation="relu"),
    tf.keras.layers.Dense(300 , activation="relu"),
    tf.keras.layers.Dense(200 , activation="relu"),
    tf.keras.layers.Dense(300 , activation="relu"),
    tf.keras.layers.Dense(4, activation="softmax")  
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss= tf.keras.losses.sparse_categorical_crossentropy,
              metrics=['accuracy'])

output = model.fit(X_train, Y_train, epochs=100)

loss, accuracy = model.evaluate(X_test, Y_test)

model.save('snake-ai_model.h5')