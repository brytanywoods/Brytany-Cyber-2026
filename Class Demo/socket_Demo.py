# Import the socket Module (Library)
import socket

# Creat TCP Socket
s = socket.socket()

# Set a time OUT
s.settimeout(1)

# Connect to a Port
result = s.connect_ex(("localhost", 80))

# Print the Result
print("Port Open" if result == 0 else "Port Closed")

# Close the Socket
s.close()