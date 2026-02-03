import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

import tensorflow as tf

FS = 3330                
WINDOW_SIZE = int(0.5 * FS)    
WINDOW_STRIDE = int(0.25 * FS)  

USE_SEQUENTIAL_SPLIT = True   #False för evaluation, True för inference över tid

X = np.load("X_features_mlp.npy")  
y = np.load("y_labels_mlp.npy")

print("X shape:", X.shape)
print("y shape:", y.shape)


#Train / test split
if USE_SEQUENTIAL_SPLIT:
    print("Sequential split, for visualization")
    split_idx = int(0.7 * len(X))
    X_train = X[:split_idx]
    y_train = y[:split_idx]
    X_test  = X[split_idx:]
    y_test  = y[split_idx:]
else:
    print("Random split, for evaluation")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.3,
        random_state=42,
        stratify=y
    )

print("Train:", X_train.shape, y_train.shape)
print("Test :", X_test.shape, y_test.shape)

np.save("X_test_mlp.npy", X_test)
np.save("y_test_mlp.npy", y_test)


window_step_sec = WINDOW_STRIDE / FS  
time_axis = np.arange(len(y_test)) * window_step_sec


#MLP model
num_classes = len(np.unique(y))

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X.shape[1],)),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(num_classes, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


#Train network
history = model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)


model.save("mlp_position_model.h5")
print("Model saved as mlp_position_model.h5")


#Prediction on test set
y_pred_prob = model.predict(X_test)
y_pred = np.argmax(y_pred_prob, axis=1)

label_names = ["lying", "moving", "standing"]
predicted_labels = [label_names[i] for i in y_pred]

print("\nOffline inference predicted labels:")
print(predicted_labels[:40]) #visar 30 första

true_labels = [label_names[i] for i in y_test]
for i in range(40):
    print(f"{i:02d}: true={true_labels[i]:9s}  pred={predicted_labels[i]}")


correct = y_pred == y_test

plt.figure(figsize=(10, 4))

plt.scatter(
    time_axis[correct],
    y_pred[correct],
    c="green",
    label="Correct",
    s=30
)

plt.scatter(
    time_axis[~correct],
    y_pred[~correct],
    c="red",
    label="Incorrect",
    s=30
)

plt.yticks([0, 1, 2], ["lying", "moving", "standing"])
plt.xlabel("Time (s)")
plt.ylabel("Predicted class")
plt.title("Offline inference MLP predictions over time")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()

#Evaluation metrics
acc = accuracy_score(y_test, y_pred)
f1_macro = f1_score(y_test, y_pred, average="macro")
f1_weighted = f1_score(y_test, y_pred, average="weighted")

print("\n Evaluation results MLP ")
print(f"Accuracy        : {acc:.4f}")
print(f"F1-score (Macro): {f1_macro:.4f}")
print(f"F1-score (Weighted): {f1_weighted:.4f}")


#Confusion matrix
cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["lying", "moving", "standing"]  
)

disp.plot(cmap="Blues")
plt.title("Confusion Matrix MLP")
plt.show()
