import sys
import serial
import time

# Default USB device /dev/ttyS0 115200 8n1
ser = serial.Serial("/dev/ttyACM0", 115200, timeout=0.5)

print('Serial test start ...')
if ser.is_open:
    print('Serial port is ready.')
else:
    print('Serial port is not ready')
    sys.exit()

def printHex(data):
    for byte in data:
        print('0x%02x' % byte, end=' ')
    print("")

def send_command(cmd):
    ser.write(cmd.encode())
    time.sleep(0.2)
    reply = ser.read(ser.in_waiting)
    print("Reply:")
    print(reply)
    printHex(reply)
    return reply

def read_qr_code():
    # Enable QR code scanning
    print("Enabling QR code scanning...")
    send_command("\x02\xf0\x03""050105"".")

    # Read QR code
    print("Reading QR code...")
    reply = send_command("\x02\xf0\x03""050101"".")

    # Process the reply to extract the QR code data
    qr_code = reply.decode().strip('\x02\x03').replace('""', '')
    print("Scanned QR Code:", qr_code)

# Check if the scanner is ready
if ser.is_open:
    print('Serial port is ready.')
else:
    print('Serial port is not ready.')
    sys.exit()

# Reset to factory defaults
print("Resetting to factory defaults...")
send_command("\x02\xf0\x03""0D0100"".")

# Set the baud rate to 115200
print("Setting baud rate to 115200...")
send_command("\x02\xf0\x03""060702115200"".")

# Get the current baud rate
print("Getting the baud rate...")
send_command("\x02\xf0\x03""060702""?.")

# Read QR codes
read_qr_code()
