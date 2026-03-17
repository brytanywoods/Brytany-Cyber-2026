import re

log = input("Enter log line:")
ip = re.search(r"\d+\.\d+\.\d+\.\d+", log)

if ip:
    print("Found IP:", ip.group())

else:
    print("No IPs found")
