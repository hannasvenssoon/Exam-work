import serial
import serial.tools.list_ports
import threading
import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
import time
from enum import Enum


POSITIONS = ["lying", "standing", "moving"]
START_COMMAND = {"log_controller":{"log_status":True}} 

class LABELS(Enum):
    LYING = 1
    STANDING = 2
    MOVING = 3


serial_port = None
is_collecting = False
current_label = None
data_rows = []

def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    return [p.device for p in ports]

def connect_serial():
    global serial_port
    port = com_select.get()

    if port == "":
        messagebox.showerror("Error", "Välj en COM-port.")
        return

    try:
        serial_port = serial.Serial(port, 115200, timeout=1)
        time.sleep(1)
        connection_status.set(f"Connected to {port}")
    except:
        messagebox.showerror("Error", f"Could not open {port}")

def start_collection():
    global is_collecting, current_label

    if serial_port is None:
        messagebox.showerror("Error", "Ingen COM-port vald.")
        return

    """if current_label is None:
        messagebox.showerror("Error", "Välj en position för datainsamling.")
        return"""

    is_collecting = True
    cmd = 'START\n'
    serial_port.write(cmd.encode("utf-8"))
    #threading.Thread(target=read_serial_data, daemon=True).start()
    serial_port.flush()
    time.sleep(0.3)  
    status_label.set("Collecting data...")
    while True:
        line = serial_port.readline().decode(errors="ignore").strip()
        if not line:
           break
        print("RX:", line)
        time.sleep(0.3) 
    

def stop_collection():
    global is_collecting
    is_collecting = False
    cmd = 'STOP\n'
    serial_port.write(cmd.encode("utf-8"))
    serial_port.flush()
    time.sleep(0.3)   
    while True:
        line = serial_port.readline().decode(errors="ignore").strip()
        if not line:
            break
        print("RX:", line)
    status_label.set("Stopped")
    get_data()

def read_serial_data():
    global is_collecting, serial_port, data_rows

    while is_collecting:
        try:
            line = serial_port.readline().decode().strip()

            if line == "":
                continue

            parts = line.split(",")

            if len(parts) == 4:
                timestamp, ax, ay, az = parts

                data_rows.append([
                    int(timestamp),
                    int(ax),
                    int(ay),
                    int(az),
                    current_label
                ])

                row_count.set(f"Rows collected: {len(data_rows)}")

        except Exception as e:
            print("Error:", e)

def get_data():
    global data_rows
    serial_port.write(b"GETDATA\n")
    serial_port.flush()
    time.sleep(0.2)
    #line = serial_port.readline().decode().strip()
    while True:
        line = serial_port.readline().decode().strip()
        if line == "DATA BEGIN":
            print("RX:", line)
            continue
        elif line == "DATA END":
            print("RX:", line)
            break
        else:
            #ts, ax, ay, az = line.split(",")
            parts = line.split(",")

            if len(parts) == 5:
                timestamp, ax, ay, az, label = parts
                match int(label):
                    case 1:
                        result = "lying"
                    case 2:
                        result = "standing"
                    case 3:
                        result = "moving"
                data_rows.append([
                    int(timestamp),
                    int(ax),
                    int(ay),
                    int(az),
                    result
                ])
            #print("RX:", line)
    row_count.set(f"Rows collected: {len(data_rows)}")

def save_dataset():
    global data_rows

    if len(data_rows) == 0:
        messagebox.showerror("Error", "Inga data att spara.")
        return

    df = pd.DataFrame(data_rows, columns=["timestamp", "ax", "ay", "az", "label"])
    filename = f"dataset_{int(time.time())}.csv"
    df.to_csv(filename, index=False)

    messagebox.showinfo("Saved", f"Dataset saved as {filename}")
    #data_rows = []
    #row_count.set("Rows collected: 0")

root = tk.Tk()
root.title("Data Collection App")
root.geometry("360x500")

tk.Label(root, text="Select COM Port:", font=("Arial", 12)).pack(pady=5)
com_select = ttk.Combobox(root, values=list_serial_ports(), width=20)
com_select.pack()

tk.Button(root, text="Refresh Ports", command=lambda: com_select.config(values=list_serial_ports())).pack()

connection_status = tk.StringVar()
connection_status.set("Not connected")
tk.Label(root, textvariable=connection_status, fg="blue").pack(pady=5)

tk.Button(root, text="Connect", width=20, command=connect_serial).pack(pady=5)

tk.Label(root, text="Select Position Label:", font=("Arial", 12)).pack(pady=10)

def set_label(lbl):
    global current_label
    current_label = lbl
    selected_label.set(f"Current label: {lbl}")

    match lbl:
        case "lying":
            result = LABELS.LYING
        case "standing":
            result = LABELS.STANDING
        case "moving":
            result = LABELS.MOVING

    cmd = f'LABEL:{result.value}\n'
    serial_port.write(cmd.encode("utf-8"))
    #threading.Thread(target=read_serial_data, daemon=True).start()
    serial_port.flush()
    time.sleep(0.3)  
    status_label.set("Setting label...")
    while True:
        line = serial_port.readline().decode(errors="ignore").strip()
        if not line:
           break
        print("RX:", line)
        time.sleep(0.3)

selected_label = tk.StringVar()
selected_label.set("Current label: None")
tk.Label(root, textvariable=selected_label, fg="green").pack()

for pos in POSITIONS:
    tk.Button(root, text=pos, width=20, command=lambda p=pos: set_label(p)).pack(pady=3)

status_label = tk.StringVar()
status_label.set("Idle")

tk.Button(root, text="Start Collection", width=20, command=start_collection).pack(pady=10)
tk.Button(root, text="Stop Collection", width=20, command=stop_collection).pack(pady=5)

tk.Label(root, textvariable=status_label, fg="purple").pack()

row_count = tk.StringVar()
row_count.set("Rows collected: 0")
tk.Label(root, textvariable=row_count).pack(pady=10)

#tk.Button(root, text="Save Dataset", width=20, command=get_data).pack(pady=10)
tk.Button(root, text="Save Dataset", width=20, command=save_dataset).pack(pady=10)

root.mainloop()


