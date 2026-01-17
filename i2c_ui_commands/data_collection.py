import os
import time
from datetime import datetime
import threading
from enum import Enum
import serial
import serial.tools.list_ports
import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSITIONS = ["lying", "standing", "moving"]
label_text = ""


class LABELS(Enum):
    LYING = 1
    STANDING = 2
    MOVING = 3


serial_port = None
reader_thread_started = False

session_data = []          
_collecting_batch = False  


def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    return [p.device for p in ports]


def connect_serial():
    global serial_port, reader_thread_started

    port = com_select.get().strip()
    if not port:
        messagebox.showerror("Error", "Välj en COM-port.")
        return

    try:
        serial_port = serial.Serial(port, 921600, timeout=1)
        time.sleep(1)
        connection_status.set(f"Connected to {port}")

        """ if not reader_thread_started:
            threading.Thread(target=serial_reader_loop, daemon=True).start()
            reader_thread_started = True """

    except Exception as e:
        messagebox.showerror("Error", f"Could not open {port}\n{e}")


def serial_reader_loop():
    global session_data, _collecting_batch, serial_port, reader_thread_started

    while reader_thread_started:
        if serial_port is None:
            time.sleep(0.1)
            continue

        try:
            line = serial_port.readline().decode(errors="ignore").strip()
        except Exception as e:
            print("RX read error:", e)
            time.sleep(0.1)
            continue

        if not line:
            continue

        if line.startswith("Measured"):
            print("RX:", line)

        """ if line == "DATA BEGIN":
            _collecting_batch = True
            continue

        if line == "DATA END":
            _collecting_batch = False
            print(f"Batch received. Total samples so far: {len(session_data)}")
            root.after(0, lambda: status_label.set("Batch received"))
            continue

        if _collecting_batch: """

        parts = line.split(",")
        #if len(parts) != 5:
        if len(parts) != 4:
            continue

        #ts, ax, ay, az, label = parts
        ts, ax, ay, az = parts

        try:
            #label_text = LABELS(int(label)).name.lower()
            row = [int(ts), int(ax), int(ay), int(az), label_text]
        except Exception:
            continue

        session_data.append(row)

        root.after(0, lambda: row_count.set(f"Rows collected: {len(session_data)}"))


def start_collection():
    global reader_thread_started
    if serial_port is None:
        messagebox.showerror("Error", "Ingen COM-port vald.")
        return
    reader_thread_started = True
    threading.Thread(target=serial_reader_loop, daemon=True).start()
    serial_port.write(b"START\n")
    serial_port.flush()
    #status_label.set("Collecting...")


def stop_collection():
    global reader_thread_started
    if serial_port is None:
        return
    reader_thread_started = False
    serial_port.write(b"STOP\n")
    serial_port.flush()
    status_label.set("Stopped")


def set_label(lbl: str):
    global label_text
    selected_label.set(f"Current label: {lbl}")
    label_text = lbl
    """ if serial_port is None:
        messagebox.showerror("Error", "Connecta COM-port först.")
        return """



    if lbl == "lying":
        code = LABELS.LYING.value
    elif lbl == "standing":
        code = LABELS.STANDING.value
    elif lbl == "moving":
        code = LABELS.MOVING.value
    else:
        messagebox.showerror("Error", f"Unknown label: {lbl}")
        return

    """ cmd = f"LABEL:{code}\n".encode("utf-8")
    serial_port.write(cmd)
    serial_port.flush() """


def save_dataset():
    global session_data

    if len(session_data) == 0:
        messagebox.showerror("Error", "Inga data att spara.")
        return

    df = pd.DataFrame(session_data, columns=["timestamp", "ax", "ay", "az", "label"])
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    #filename = os.path.join(BASE_DIR, f"dataset_{int(time.time())}.csv")
    filename = os.path.join(BASE_DIR, f"dataset_{timestamp}.csv")
    df.to_csv(filename, index=False)

    messagebox.showinfo("Saved", f"Dataset saved as:\n{filename}\nSamples: {len(session_data)}")

    session_data = []
    row_count.set("Rows collected: 0")
    status_label.set("Idle")


root = tk.Tk()
root.title("Data Collection App")
root.geometry("360x520")

tk.Label(root, text="Select COM Port:", font=("Arial", 12)).pack(pady=5)
com_select = ttk.Combobox(root, values=list_serial_ports(), width=20)
com_select.pack()

tk.Button(root, text="Refresh Ports",
          command=lambda: com_select.config(values=list_serial_ports())).pack(pady=4)

connection_status = tk.StringVar(value="Not connected")
tk.Label(root, textvariable=connection_status, fg="blue").pack(pady=5)

tk.Button(root, text="Connect", width=20, command=connect_serial).pack(pady=5)

tk.Label(root, text="Select Position Label:", font=("Arial", 12)).pack(pady=10)

selected_label = tk.StringVar(value="Current label: None")
tk.Label(root, textvariable=selected_label, fg="green").pack()

for pos in POSITIONS:
    tk.Button(root, text=pos, width=20, command=lambda p=pos: set_label(p)).pack(pady=3)

status_label = tk.StringVar(value="Idle")
tk.Label(root, textvariable=status_label, fg="purple").pack(pady=10)

tk.Button(root, text="Start Collection", width=20, command=start_collection).pack(pady=6)
tk.Button(root, text="Stop Collection", width=20, command=stop_collection).pack(pady=4)

row_count = tk.StringVar(value="Rows collected: 0")
tk.Label(root, textvariable=row_count).pack(pady=10)

tk.Button(root, text="Save Dataset", width=20, command=save_dataset).pack(pady=10)

root.mainloop()
