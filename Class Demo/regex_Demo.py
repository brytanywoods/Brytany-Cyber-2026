# Import Pythons Regular Expression Module
import re

# Crate a log Entry
log = "Error from 192.168.1.1"

# Search the log for an IP address
ip= re.search(r"\d+\.\d+\.\d+\.\d+", log)

# Check if a Match was found
if ip:
    print("Found IP:", ip.group())
else:
    print("No Ip's found")
