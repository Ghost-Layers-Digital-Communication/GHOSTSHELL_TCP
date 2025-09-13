# listener_tcp.py
import socket
import threading
import subprocess
import os

PORT = xxxx # PORT NUMBER

def show_ascii(name):
    path = f"ascii/{name}.txt"
    try:
        with open(path, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"[ERROR] ASCII art file '{path}' not found.")

def show_banner():
    try:
        with open("ascii/ghostshell_banner.txt", "r") as banner:
            print(banner.read())
    except FileNotFoundError:
        print("[BANNER] Ghost Shell startup banner not found.")

def execute_payload(script):
    show_ascii('tango_delta')
    payload_path = f"/home/xxxxxxx/Desktop/GhostShell_TCP1/{script}" # USER NAME IN X'S
    if os.path.exists(payload_path):
        subprocess.call(["python3", payload_path])
    else:
        print(f"[ERROR] Payload {payload_path} not found.")

def check_payload():
    payload_path = "/home/xxxxxxx/Desktop/GhostShell_TCP1/td_script.py" #USER NAME IN X'S
    if os.path.exists(payload_path):
        show_ascii('payload_detected')
    else:
        print("[STATUS] No payload found.")

def handle_client(conn, addr):
    print(f"[CONNECTED] {addr} connected.")
    with conn:
        while True:
            data = conn.recv(1024).decode('utf-8').strip()
            if not data:
                break
            print(f"[COMMAND RECEIVED] {data}")

            if data == "CONNECT":
                show_ascii('connected')
            elif data == "STATUS":
                check_payload()
            elif data == "TD":
                execute_payload("td_script.py")
            elif data == "DISCONNECT":
                show_ascii('disconnected')
            else:
                print(f"[WARNING] Unknown command: {data}")

    print(f"[DISCONNECTED] {addr} disconnected.")

def start_listener():
    show_banner()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', PORT))
        s.listen()
        print(f"[LISTENER] Listening on port {PORT}...")
        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    start_listener()