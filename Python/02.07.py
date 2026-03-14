# user _parser.py

users ={
    "alice": {"ip": "192.168.1.1", "login": "2025-06-20"},
    "bob": {"ip": "10.0.0.1", "login": "2025-06-19"}
    }

for  user, info in users.items():
    print(f"User: {user}, IP: {info['ip']}, Last Login: {info['login']}")

