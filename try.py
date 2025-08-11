import serial

# Change COM3 to your Arduino's port, 9600 must match Serial.begin()
ser = serial.Serial('COM10', 9600)

print("Reading from Arduino...")
while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print(line)
    except KeyboardInterrupt:
        print("\nExiting...")
        break
    except Exception as e:
        print("Error:", e)
        break

ser.close()
