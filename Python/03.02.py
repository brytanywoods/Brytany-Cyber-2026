#Important OS

import os

def list_directories(path):
    try:

        items = os.listdir(path)
        for item in items:
            if os.path.isdir(os.path.join(path, item)):
                print(item)
    except PermissionError:
        print("Permission denied to access the directory.")