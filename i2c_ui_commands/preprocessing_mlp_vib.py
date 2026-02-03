import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

CSV_NORMAL   = "dataset_normal_2026-01-20_15-29-16.csv"
CSV_ABNORMAL = "dataset_abnormal30hz_2026-01-20_15-39-23.csv"

AXES = ["ax", "ay", "az"]

LABEL_MAP = {
    "normal": 0,
    "abnormal": 1
}

WINDOW_SIZE = 128
OVERLAP = 64
STEP = WINDOW_SIZE - OVERLAP

FULL_SCALE_G = 4.0
LSB_PER_G = 32768 / FULL_SCALE_G

df_normal = pd.read_csv(CSV_NORMAL)
df_abnormal = pd.read_csv(CSV_ABNORMAL)

acc_normal = df_normal[AXES].values.astype(np.float32)
acc_abnormal = df_abnormal[AXES].values.astype(np.float32)

acc_normal_mg = (acc_normal / LSB_PER_G) * 1000.0
acc_abnormal_mg = (acc_abnormal / LSB_PER_G) * 1000.0


def extract_features(window):
    features = []
    for axis in range(3):
        sig = window[:, axis]
        features.extend([
            np.mean(sig),
            np.std(sig),
            np.min(sig),
            np.max(sig),
            np.sqrt(np.mean(sig ** 2))  # RMS
        ])
    return features

def create_windows(acc, label_id):
    X, y = [], []
    for start in range(0, len(acc) - WINDOW_SIZE + 1, STEP):
        window = acc[start:start + WINDOW_SIZE]
        X.append(extract_features(window))
        y.append(label_id)
    return np.array(X), np.array(y)

X_normal, y_normal = create_windows(acc_normal_mg, LABEL_MAP["normal"])
X_abnormal, y_abnormal = create_windows(acc_abnormal_mg, LABEL_MAP["abnormal"])

X = np.vstack([X_normal, X_abnormal])
y = np.concatenate([y_normal, y_abnormal])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

rng = np.random.default_rng(42)
idx = rng.permutation(len(X_scaled))
X_scaled, y = X_scaled[idx], y[idx]

np.save("X_features_mlp_vib.npy", X_scaled)
np.save("y_labels_mlp_vib.npy", y)

np.save("scaler_mean_mlp_vib.npy", scaler.mean_)
np.save("scaler_scale_mlp_vib.npy", scaler.scale_)

FEATURE_NAMES = [
    "mean_x", "std_x", "min_x", "max_x", "rms_x",
    "mean_y", "std_y", "min_y", "max_y", "rms_y",
    "mean_z", "std_z", "min_z", "max_z", "rms_z"
]
np.save("feature_names_mlp_vib.npy", FEATURE_NAMES)

assert X_scaled.shape[1] == 15
assert len(np.unique(y)) == 2

print("Preprocessing klar")
print("X shape:", X_scaled.shape)
print("y shape:", y.shape)
print("Label distribution:", np.bincount(y))
