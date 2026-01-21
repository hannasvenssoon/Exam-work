import serial
import csv
import time

PORT = "COM3"        
BAUD = 921600
OUT_FILE = "fifo_test.csv"

ser = serial.Serial(PORT, BAUD, timeout=2)
time.sleep(2)  

samples = []
recording = False

print("Listening...")

while True:
    line = ser.readline().decode(errors="ignore").strip()

    if not line:
        continue

    if line == "DATA BEGIN":
        print("Receiving data...")
        recording = True
        continue

    if line == "DATA END":
        print(f"Done. Samples: {len(samples)}")
        break

    if recording:
        try:
            ts, ax, ay, az = map(int, line.split(","))
            samples.append([ts, ax, ay, az])
        except ValueError:
            pass

ser.close()

# Spara till CSV
with open(OUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "ax", "ay", "az"])
    writer.writerows(samples)

print(f"Saved to {OUT_FILE}")
