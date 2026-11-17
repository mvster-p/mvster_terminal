import serial
import time
import os
from datetime import datetime

# ==========================
# CONFIG
# ==========================

PORT = "COM8"      # Your Leonardo
BAUD = 115200
LOG_DIR = "logs"
RECONNECT_DELAY = 3


# ==========================
# HELPERS
# ==========================

def now():
    return datetime.now()


def make_log_file():
    date_folder = now().strftime("%Y-%m-%d")
    time_name = now().strftime("%H-%M-%S")

    folder = os.path.join(LOG_DIR, date_folder)
    os.makedirs(folder, exist_ok=True)

    filename = f"session_{time_name}.txt"
    return os.path.join(folder, filename)


def connect():
    while True:
        try:
            print(f"[+] Connecting to {PORT}...")
            ser = serial.Serial(PORT, BAUD, timeout=1)
            print("[+] Connected.")
            return ser
        except:
            print("[-] Waiting for device...")
            time.sleep(RECONNECT_DELAY)


# ==========================
# MAIN
# ==========================

def main():

    print("=== NYX SERIAL LOGGER ===")
    print("Port:", PORT)
    print("Press CTRL+C to exit\n")

    os.makedirs(LOG_DIR, exist_ok=True)

    log_file = make_log_file()
    print("[+] Logging to:", log_file)

    ser = connect()

    with open(log_file, "a", encoding="utf-8") as f:

        f.write("=== SESSION START ===\n")

        while True:

            try:
                if ser.in_waiting:

                    data = ser.read(ser.in_waiting).decode(errors="ignore")

                    timestamp = now().strftime("[%H:%M:%S] ")

                    line = timestamp + data

                    # Show live
                    print(line, end="", flush=True)

                    # Save
                    f.write(line)
                    f.flush()

            except serial.SerialException:
                print("\n[!] Disconnected.")
                ser.close()
                ser = connect()

            except KeyboardInterrupt:
                print("\n[+] Logger stopped.")
                f.write("\n=== SESSION END ===\n")
                ser.close()
                break


if __name__ == "__main__":
    main()