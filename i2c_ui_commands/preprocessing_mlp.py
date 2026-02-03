import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder


CSV_PATH = "dataset_lying_2026-01-19_10-11-39.csv" 
FS = 3330               
WINDOW_SIZE = int(0.5 * FS)  
WINDOW_STRIDE = int(0.25 * FS)  

FULL_SCALE_G = 4.0          
LSB_PER_G = 32768 / FULL_SCALE_G


df = pd.read_csv(CSV_PATH)

df = df.sort_values("timestamp").reset_index(drop=True)


df["ax_mg"] = (df["ax"] / LSB_PER_G) * 1000
df["ay_mg"] = (df["ay"] / LSB_PER_G) * 1000
df["az_mg"] = (df["az"] / LSB_PER_G) * 1000


#Ta bort eventuella dubletter
df = df.drop_duplicates(subset=["timestamp", "ax", "ay", "az"])

#Sliding window
def sliding_windows(data, labels, win_size, stride):
    X, y = [], []
    for start in range(0, len(data) - win_size, stride):
        end = start + win_size
        window = data[start:end]
        label = labels[start:end]

        # Majoritetslabel
        majority_label = label.mode()[0]

        X.append(window)
        y.append(majority_label)

    return np.array(X), np.array(y)

signals = df[["ax_mg", "ay_mg", "az_mg"]]
labels = df["label"]

X_raw, y_raw = sliding_windows(
    signals, labels, WINDOW_SIZE, WINDOW_STRIDE
)


#Feature extraction
def extract_features(window):
    features = []

    for axis in range(3):
        sig = window[:, axis]
        features.extend([
            np.mean(sig),
            np.std(sig),
            np.min(sig),
            np.max(sig),
            np.sqrt(np.mean(sig**2))  
        ])

    return features

X_features = np.array([extract_features(w) for w in X_raw])

#Normalisering / Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_features)
np.save("scaler_mean_mlp.npy", scaler.mean_)
np.save("scaler_scale_mlp.npy", scaler.scale_)


#Label encoding
le = LabelEncoder()
y_encoded = le.fit_transform(y_raw)

np.save("classes_mlp.npy", le.classes_)

print("Labels:", dict(zip(le.classes_, le.transform(le.classes_))))


np.save("X_features_mlp.npy", X_scaled)
np.save("y_labels_mlp.npy", y_encoded)


print("Preprocessing klar!")
print("X shape:", X_scaled.shape)
print("y shape:", y_encoded.shape)

