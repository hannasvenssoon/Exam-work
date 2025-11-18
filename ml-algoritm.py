import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv ("acc_full_data.csv", sep = ';', names=["x", "y", "z", "label"])

X = df[["x", "y", "z"]].values.astype("float32")
y = df["label"].values

X_tf = tf.convert_to_tensor(X)
y_tf = tf.convert_to_tensor(y)

print("Loaded shape: ", X_tf.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)



def euclidean_distance(X_train, X_test_point):
    distances = tf.sqrt(tf.reduce_sum(tf.square(X_train - X_test_point), axis=1))
    return distances


def knn(X_train, y_train, X_test, K):
    y_pred = []

    for X_test_point in X_test:
        distances = euclidean_distance(X_train, X_test_point)
        nearest_neighbors = tf.argsort(distances)[:K]
        nearest_labels = y_train[nearest_neighbors.numpy()]
        #nearest_labels = nearest_labels.numpy()       

        values, counts = np.unique(nearest_labels, return_counts = True)
        predicted_label = values[np.argmax(counts)]
        y_pred.append(predicted_label)

    return np.array(y_pred)


k_values = [3,5,7,9]

for k in k_values:
    y_pred = knn(X_train, y_train, X_test, k)
    accuracy = np.mean(y_pred == y_test)
    print(f"KNN Model Accuracy (k = {k}): {accuracy * 100:.2f}%")



def predict_position(X_train, y_train, new_point, k):
    new_point_scaled = scaler.transform([new_point])

    distances = euclidean_distance(X_train, new_point_scaled[0])

    nearest_neighbors = tf.argsort(distances)[:k]
    nearest_labels = y_train[nearest_neighbors.numpy()]
    values, counts = np.unique(nearest_labels, return_counts = True)
    predicted_label = values [np.argmax(counts)]
    return predicted_label


new_point = [-4, 1072, 20]
k = 5
prediction = predict_position(X_train, y_train, new_point, k)
print(f"Predicted position: {prediction}")

