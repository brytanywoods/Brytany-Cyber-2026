# Connect to a Port
import socket

host = input("Enter a host: ")
ports = [80, 443]
for port in ports:
    try:
        
print("Port Open" if result == 0 else "Port Closed")