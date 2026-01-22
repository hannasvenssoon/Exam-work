import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)
from sklearn.utils.class_weight import compute_class_weight

WINDOW_SIZE = 128
OVERLAP = 64
step = WINDOW_SIZE - OVERLAP

USE_SEQUENTIAL_SPLIT = True   # False = evaluation, True = inference över tid
LABEL_NAMES = ["lying", "moving", "standing"]


X = np.load("X_cnn.npy")    # (N, 128, 3)
y = np.load("y_cnn.npy")    # (N,)

print("X shape:", X.shape)
print("y shape:", y.shape)
print("Unique labels:", np.unique(y))
print("Label distribution:", np.bincount(y))

assert X.ndim == 3
assert len(X) == len(y)

num_classes = len(np.unique(y))


if USE_SEQUENTIAL_SPLIT:
    print("Sequential split (visualization)")
    split_idx = int(0.7 * len(X))
    X_train = X[:split_idx]
    y_train = y[:split_idx]
    X_test  = X[split_idx:]
    y_test  = y[split_idx:]
else:
    print("Random split (evaluation)")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.3,
        random_state=42,
        stratify=y
    )

print("Train:", X_train.shape, y_train.shape)
print("Test :", X_test.shape, y_test.shape)

FS = 3330

STEP = WINDOW_SIZE - OVERLAP

time_test = np.arange(len(y_test)) * (STEP / FS)

inputs = tf.keras.Input(shape=X.shape[1:])  # (128, 3)

x = tf.keras.layers.Conv1D(16, 5, padding="same", activation="relu")(inputs)
x = tf.keras.layers.MaxPool1D(2)(x)

x = tf.keras.layers.Conv1D(32, 5, padding="same", activation="relu")(x)
x = tf.keras.layers.MaxPool1D(2)(x)

x = tf.keras.layers.Conv1D(64, 3, padding="same", activation="relu")(x)

x = tf.keras.layers.GlobalAveragePooling1D()(x)
x = tf.keras.layers.Dense(64, activation="relu")(x)
x = tf.keras.layers.Dropout(0.2)(x)

outputs = tf.keras.layers.Dense(num_classes, activation="softmax")(x)

model = tf.keras.Model(inputs, outputs)
model.summary()


model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-3),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


class_weights = compute_class_weight(
    class_weight="balanced",
    classes=np.unique(y_train),
    y=y_train
)
class_weights = dict(zip(np.unique(y_train), class_weights))
print("Class weights:", class_weights)


callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor="val_loss", patience=10, restore_best_weights=True
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor="val_loss", factor=0.5, patience=5, min_lr=1e-5
    ),
]

history = model.fit(
    X_train, y_train,
    epochs=60,
    batch_size=64,
    validation_split=0.2,
    class_weight=class_weights,
    callbacks=callbacks,
    verbose=1
)

model.save("cnn_model.h5")
print("Model saved as cnn_model.h5")


y_pred_prob = model.predict(X_test, verbose=0)
y_pred = np.argmax(y_pred_prob, axis=1)

predicted_labels = [LABEL_NAMES[i] for i in y_pred]
true_labels = [LABEL_NAMES[i] for i in y_test]

print("\nOffline inference predicted labels:")
print(predicted_labels[:40])

for i in range(min(40, len(y_test))):
    print(f"{i:02d}: true={true_labels[i]:9s}  pred={predicted_labels[i]}")


if USE_SEQUENTIAL_SPLIT:
    correct = y_pred == y_test

    plt.figure(figsize=(10, 4))

    plt.scatter(
        time_test[correct],
        y_pred[correct],
        c="green",
        label="Correct",
        s=30
    )

    plt.scatter(
        time_test[~correct],
        y_pred[~correct],
        c = "red",
        label="Incorrect",
        s=30
    )

    plt.yticks([0, 1, 2], LABEL_NAMES)
    plt.xlabel("Time (s)")
    plt.ylabel("Predicted class")
    plt.title("Offline inference CNN predictions over time")
    plt.grid(axis="y", linestyle="--", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


acc = accuracy_score(y_test, y_pred)
f1_macro = f1_score(y_test, y_pred, average="macro")
f1_weighted = f1_score(y_test, y_pred, average="weighted")

print("\nEvaluation results CNN")
print(f"Accuracy        : {acc:.4f}")
print(f"F1-score (Macro): {f1_macro:.4f}")
print(f"F1-score (Weighted): {f1_weighted:.4f}")


if not USE_SEQUENTIAL_SPLIT:
    cm = confusion_matrix(y_test, y_pred)

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=LABEL_NAMES
    )

    disp.plot(cmap="Blues")
    plt.title("Confusion Matrix CNN")
    plt.show()
