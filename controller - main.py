# controller_tcp.py
import socket

PI_IP = "xxx.xxx.xxx.xxx" # LAN IP
PORT = xxxx # PORT NUMBER

ascii_map = {
    "CONNECT": "connected",
    "STATUS": "payload_detected",
    "TD": "tango_delta",
    "DISCONNECT": "disconnected"
}

def show_ascii(name):
    path = f"ascii/{name}.txt"
    try:
        with open(path, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"[ERROR] ASCII art file '{path}' not found.")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((PI_IP, PORT))
        except ConnectionRefusedError:
            print("Cannot connect. Make sure listener is running on other box.")
            return
        print(f"Connected to BUGALOO at {PI_IP}:{PORT}")

        while True:
            cmd = input("Enter Command [CONNECT / STATUS / TD / DISCONNECT] or Q to quit: ").upper()
            if cmd == 'Q':
                break
            if cmd in ascii_map:
                show_ascii(ascii_map[cmd]) # optional local preview
                s.sendall(cmd.encode('utf-8'))
            else:
                print("[INPUT] Invalid Command.")

if __name__ == "__main__":
    main()
