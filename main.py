import keyboard

def on_key_press(event):
    if event.name == 'enter':
        # Process the scanned QR code
        qr_code = ''
        while True:
            key_event = keyboard.read_event()
            if key_event.name == 'enter':
                break
            qr_code += key_event.name

        print(f"Scanned QR Code: {qr_code}")

keyboard.on_press(on_key_press)
keyboard.wait('esc')  # Wait for the 'esc' key to exit the script
