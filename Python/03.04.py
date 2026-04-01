#Find .txt files

"*.txt "
import os

try:
    happylab = os.listdir("/home")
    print(happylab)
except Exception as e:
    print(e)

