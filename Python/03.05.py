# Example of using os module to list files in a directory and check permissions

import os
import stat
def list_files_with_permissions(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                permissions = os.stat(file_path).st_mode
                is_writable_by_others = bool(permissions & stat.S_IWOTH)
                print(f"{file_path} - Writable by others: {is_writable_by_others}")

            except FileNotFoundError:
                continue

            except PermissionError:
                print("Permission denied to access the directory.")
list_files_with_permissions("/home/kali")




