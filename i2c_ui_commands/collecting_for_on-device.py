# import serial

# ser = serial.Serial("COM3", 115200, timeout=1)

# print("Listening...")

# while True:
#     line = ser.readline().decode(errors="ignore").strip()
#     if line:
#         print(line)

import serial

ser = serial.Serial("COM3", 115200, timeout=1)

preds = []
labels = []

print("Listening... Ctrl+C to stop")

try:
    while True:
        line = ser.readline().decode(errors="ignore").strip()
        if line.startswith("PRED:"):
            parts = line.split(",")
            pred = int(parts[0].split(":")[1])
            label = int(parts[1].split(":")[1])

            preds.append(pred)
            labels.append(label)

except KeyboardInterrupt:
    pass

import numpy as np
np.save("y_pred_device.npy", np.array(preds))
np.save("y_true_device.npy", np.array(labels))

