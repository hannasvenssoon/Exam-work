import numpy as np
from sklearn.metrics import accuracy_score, f1_score

y_pred = np.load("y_pred_device.npy")
y_true = np.load("y_true_device.npy")

print("=== On-device inference ===")
print("Accuracy        :", accuracy_score(y_true, y_pred))
print("F1-score Macro  :", f1_score(y_true, y_pred, average="macro"))
print("F1-score Weight :", f1_score(y_true, y_pred, average="weighted"))
