#Write a Python script to list user from etc/passwd reinforcing user management

etc_passwd = "/etc/passwd"

with open(etc_passwd, "r") as f:
    for line in f:
        user = line.split(":")[0]
        print(user)