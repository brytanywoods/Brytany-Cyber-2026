# Write a Python script to list group members from '/etc/group'

etc_group = "/etc/group"

with open(etc_group, "r") as f:
    for line in f:
        group = line.split(":")[0]
        members = line.split(":")[3].split(",")
        print(f"Group: {group}")
        print(f"Members: {members}")