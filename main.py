import serial
import sys

def read_qr_code():
    try:
        ser = serial.Serial("/dev/tty.usbmodemS220827007721", 115200, timeout=0.1)
        print("Connected to the QR code scanner.")
    except serial.SerialException:
        print("Failed to connect to the QR code scanner.")
        sys.exit(1)

    while True:
        line = ser.readline().decode().strip()
        if line:
            print("QR code:", line)

    ser.close()

read_qr_code()