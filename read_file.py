import serial
import csv

SERIAL_PORT = 'COM3'
SERIAL_RATE = 115200
FILE1 = "acc_liggande_data.csv"
FILE2 = "acc_stående_data.csv"
FILE3 = "acc_lutad_data.csv"
FILE4 = "acc_rorelse_data.csv"

def main():
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)

    with open(FILE1, mode = 'w', newline = '') as file:
        write = csv.writer(file, delimiter= ';')

        print('Samlar data till ' + FILE1)
        while True:
            read = ser.readline().decode('utf-8').strip()

            if read:
                parts = read.split(',')
                if len(parts) == 3:
                    write.writerow(parts)
                    file.flush()

                print(read)





if __name__ == "__main__":
    main()