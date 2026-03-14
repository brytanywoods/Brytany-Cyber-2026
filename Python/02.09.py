# Connect to a Port
import socket

host = input("Enter a host: ")
ports = [80, 443]
for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open on {host}")
        sock.close()
    except Exception:
        print(f"Error connecting to {host}:{port}")