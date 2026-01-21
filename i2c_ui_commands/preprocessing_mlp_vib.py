import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder


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

for col in AXES:
    if col not in df_normal.columns or col not in df_abnormal.columns:
        raise ValueError(f"Saknar kolumn: {col}")

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


def create_windows(acc_norm, label_id):
    X, y = [], []
    for start in range(0, len(acc_norm) - WINDOW_SIZE + 1, STEP):
        window = acc_norm[start:start + WINDOW_SIZE]
        X.append(extract_features(window))
        y.append(label_id)
    return np.array(X), np.array(y)


scaler = StandardScaler()
acc_all = np.vstack([acc_normal_mg, acc_abnormal_mg])
acc_all_norm = scaler.fit_transform(acc_all)

np.save("scaler_mean_mlp_vib.npy", scaler.mean_)
np.save("scaler_scale_mlp_vib.npy", scaler.scale_)

acc_normal_norm = acc_all_norm[:len(acc_normal_mg)]
acc_abnormal_norm = acc_all_norm[len(acc_normal_mg):]


X_normal, y_normal = create_windows(acc_normal_norm, LABEL_MAP["normal"])
X_abnormal, y_abnormal = create_windows(acc_abnormal_norm, LABEL_MAP["abnormal"])

print("Normal windows :", len(y_normal))
print("Abnormal windows:", len(y_abnormal))

X = np.vstack([X_normal, X_abnormal])
y = np.concatenate([y_normal, y_abnormal])

# Shuffle
rng = np.random.default_rng(42)
idx = rng.permutation(len(X))
X, y = X[idx], y[idx]


#Sanity check
assert X.shape[0] == y.shape[0], "X och y har olika längd!"
assert X.shape[1] == 15, "MLP ska ha exakt 15 features"
assert len(np.unique(y)) == 2, "Datasetet ska vara binärt (normal/abnormal)"

FEATURE_NAMES = [
    "mean_x", "std_x", "min_x", "max_x", "rms_x",
    "mean_y", "std_y", "min_y", "max_y", "rms_y",
    "mean_z", "std_z", "min_z", "max_z", "rms_z"
]

np.save("feature_names_mlp_vib.npy", FEATURE_NAMES)

np.save("X_features_mlp_vib.npy", X)
np.save("y_labels_mlp_vib.npy", y)

print("Preprocessing klar")
print("X shape:", X.shape)
print("y shape:", y.shape)
print("Label distribution:", np.bincount(y))
