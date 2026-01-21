import numpy as np

mean = np.load("scaler_mean.npy")
scale = np.load("scaler_scale.npy")

print("Klistra in detta i scaler_mean[15]:")
print(", ".join([f"{v}f" for v in mean]))

print("\nKlistra in detta i scaler_scale[15]:")
print(", ".join([f"{v}f" for v in scale]))      # Kommer visa alla 15 värden


classes = np.load("classes.npy", allow_pickle=True)
print(classes)