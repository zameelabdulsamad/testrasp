import subprocess
import time
import serial

def power_off_usb_device(device_path):
    subprocess.run(['sudo', 'usbreset', device_path])

def power_on_usb_device(device_path):
    subprocess.run(['sudo', 'usbreset', device_path])

def read_qr_code():
    try:
        # Open serial connection
        ser = serial.Serial("/dev/ttyACM0", 115200, timeout=0.1)
        print("Connected to the QR code scanner.")
    except serial.SerialException:
        print("Failed to connect to the QR code scanner.")
        sys.exit(1)

    # Determine the USB device path for /dev/ttyACM0
    device_path = ser.port

    power_off_usb_device(device_path)
    time.sleep(10)  # Sleep for 10 seconds

    power_on_usb_device(device_path)

    while True:
        line = ser.readline().decode().strip()
        if line:
            print("QR code:", line)

    ser.close()

read_qr_code()
