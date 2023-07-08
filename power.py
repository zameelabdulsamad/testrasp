import subprocess

def turn_off_usb_port(port_number):
    command = f"sudo ./hub-ctrl -h 0 -P {port_number} -p 0"
    subprocess.call(command, shell=True)

# Example usage: Turn off power to USB port 1
turn_off_usb_port(2)