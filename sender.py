import serial

ser = serial.Serial("COM8", 115200)

print("Connected. Type to send.\n")

while True:
    msg = input("> ")
    ser.write(msg.encode())