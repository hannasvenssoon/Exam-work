import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


CSV_FILE = "dataset_lying_2026-01-19_10-11-39.csv"

WINDOW_SIZE = 128
OVERLAP = 64

AXES = ["ax", "ay", "az"]

LABEL_MAP = {
    "lying": 0,
    "standing": 1,
    "moving": 2,
}

FULL_SCALE_G = 4.0          
LSB_PER_G = 32768 / FULL_SCALE_G


df = pd.read_csv(CSV_FILE)

# Kolla att allt finns
for col in AXES + ["label"]:
    if col not in df.columns:
        raise ValueError(f"Saknar kolumn: {col}")

acc = df[AXES].values.astype(np.float32)

acc_g = acc / LSB_PER_G
acc_mg = acc_g * 1000.0

#Normalisering
scaler = StandardScaler()
acc_norm = scaler.fit_transform(acc_mg)

mean = scaler.mean_
std = scaler.scale_

#Sliding windows
X = []
y = []

step = WINDOW_SIZE - OVERLAP

for start in range(0, len(acc_norm) - WINDOW_SIZE + 1, step):
    # window data
    X.append(acc_norm[start:start + WINDOW_SIZE])

    # Majority vote label
    window_labels = df["label"].iloc[start:start + WINDOW_SIZE]
    label_str = window_labels.mode()[0]
    y.append(LABEL_MAP[label_str])


X = np.array(X, dtype=np.float32)
y = np.array(y, dtype=np.int32)

print("Unique labels:", np.unique(y))
print("Label distribution:", np.bincount(y))
print("X shape:", X.shape)  #(N, 128, 3) --> n antal fönster, tidsdimension, 3 axlar
print("y shape:", y.shape)

assert len(np.unique(y)) >= 2, "FEL: bara en klass i y!"


np.save("X_cnn.npy", X)
np.save("y_cnn.npy", y)
np.save("scaler_cnn_mean.npy", mean)
np.save("scaler_cnn_std.npy", std)

print("Preprocessing done!")

