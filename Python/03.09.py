# Write a Python script to list files owned by a specific user, reinforcing auditing skills

import os
import pwd

def list_files_owned_by_user(username):
    try:
        user_files = []
        for root, dirs, files in os.walk("/"):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path) and os.stat(file_path).st_uid == pwd.getpwnam(username).pw_uid:
                    user_files.append(file_path)
        print(f"Files owned by {username}:")
        for user_file in user_files:
            print(user_file)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    list_files_owned_by_user("kali") 