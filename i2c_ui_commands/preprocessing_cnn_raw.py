import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


CSV_NORMAL   = "dataset_normal_2026-01-20_15-29-16.csv"
CSV_ABNORMAL = "dataset_abnormal30hz_2026-01-20_15-39-23.csv"

WINDOW_SIZE = 128
OVERLAP     = 64
STEP        = WINDOW_SIZE - OVERLAP

AXES = ["ax", "ay", "az"]

LABEL_MAP = {
    "normal": 0,
    "abnormal": 1,
}

FULL_SCALE_G = 4.0
LSB_PER_G = 32768 / FULL_SCALE_G  


def create_windows(acc_norm, label_id):
    X = []
    y = []

    for start in range(0, len(acc_norm) - WINDOW_SIZE + 1, STEP):
        window = acc_norm[start:start + WINDOW_SIZE]
        X.append(window)
        y.append(label_id)

    return np.array(X, dtype=np.float32), np.array(y, dtype=np.int32)


df_normal   = pd.read_csv(CSV_NORMAL)
df_abnormal = pd.read_csv(CSV_ABNORMAL)

for col in AXES:
    if col not in df_normal.columns or col not in df_abnormal.columns:
        raise ValueError(f"Saknar kolumn: {col}")


acc_normal = df_normal[AXES].values.astype(np.float32)
acc_abnormal = df_abnormal[AXES].values.astype(np.float32)

acc_normal_g = acc_normal / LSB_PER_G
acc_abnormal_g = acc_abnormal / LSB_PER_G

acc_normal_mg = acc_normal_g * 1000.0
acc_abnormal_mg = acc_abnormal_g * 1000.0


scaler = StandardScaler()

acc_all_mg = np.vstack([acc_normal_mg, acc_abnormal_mg])
acc_all_norm = scaler.fit_transform(acc_all_mg)

np.save("scaler_vib_mean.npy", scaler.mean_)
np.save("scaler_vib_std.npy", scaler.scale_)


acc_normal_norm = acc_all_norm[:len(acc_normal_mg)]
acc_abnormal_norm = acc_all_norm[len(acc_normal_mg):]


X_normal, y_normal = create_windows(
    acc_normal_norm,
    LABEL_MAP["normal"]
)

X_abnormal, y_abnormal = create_windows(
    acc_abnormal_norm,
    LABEL_MAP["abnormal"]
)

print("Normal windows  :", X_normal.shape)
print("Abnormal windows:", X_abnormal.shape)


X = np.concatenate([X_normal, X_abnormal], axis=0)
y = np.concatenate([y_normal, y_abnormal], axis=0)

rng = np.random.default_rng(seed=42)
idx = rng.permutation(len(X))
X = X[idx]
y = y[idx]

print("Total windows:", X.shape)
print("Label distribution:", np.bincount(y))

assert len(np.unique(y)) == 2, "FEL: båda klasserna måste finnas!"


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

print("Train:", X_train.shape, y_train.shape)
print("Test :", X_test.shape, y_test.shape)


np.save("X_train_cnn_vib.npy", X_train)
np.save("y_train_cnn_vib.npy", y_train)
np.save("X_test_cnn_vib.npy",  X_test)
np.save("y_test_cnn_vib.npy",  y_test)

print("\nPreprocessing done")
