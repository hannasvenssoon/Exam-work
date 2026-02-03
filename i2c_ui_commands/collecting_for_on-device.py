import serial

ser = serial.Serial("COM3", 115200, timeout=1)

print("Listening...")

while True:
    line = ser.readline().decode(errors="ignore").strip()
    if line:
        print(line)

"""import serial
import sys
import threading
from sklearn.metrics import accuracy_score, f1_score

PORT = "COM3"
BAUD = 115200

# 0 = LYING, 1 = MOVING, 2 = STANDING
current_label = 0

y_true = []
y_pred = []

ser = serial.Serial(PORT, BAUD, timeout=1)

print("Listening...")
print("Press 0=LYING, 1=MOVING, 2=STANDING")
print("Press q to quit & compute metrics")

def keyboard_listener():
    global current_label
    while True:
        key = sys.stdin.read(1)
        if key == "0":
            current_label = 0
            print("\nSwitched to LYING")
        elif key == "1":
            current_label = 1
            print("\nSwitched to MOVING")
        elif key == "2":
            current_label = 2
            print("\nSwitched to STANDING")
        elif key.lower() == "q":
            break


threading.Thread(target=keyboard_listener, daemon=True).start()

try:
    while True:
        line = ser.readline().decode(errors="ignore").strip()
        if not line:
            continue

        if line.startswith("PRED:"):
            parts = line.split()
            pred = int(parts[1])

            y_pred.append(pred)
            y_true.append(current_label)

            print(f"PRED= {pred}  Current label= {current_label}")

except KeyboardInterrupt:
    pass

print("\nStopping...")


acc = accuracy_score(y_true, y_pred)
f1_macro = f1_score(y_true, y_pred, average="macro")
f1_weighted = f1_score(y_true, y_pred, average="weighted")

print("\nON-DEVICE INFERENCE RESULTS")
print(f"Accuracy           : {acc:.4f}")
print(f"F1-score (Macro)   : {f1_macro:.4f}")
print(f"F1-score (Weighted): {f1_weighted:.4f}")

ser.close()"""


