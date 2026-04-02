# Write a Python script to list SUID files, reinforcing permission audits

import os

try:
    suid_files = []
    for root, dirs, files in os.walk("/"):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path) and os.stat(file_path).st_mode & 0o4000:
                suid_files.append(file_path)
    print("SUID files found:")
    for suid_file in suid_files:
        print(suid_file)
except Exception as e:
    print(e)