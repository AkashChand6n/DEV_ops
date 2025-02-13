import os
print("current working dir:",os.getcwd())
try:
    f = open("file.txt")
    print(f.read())
finally:
    f.close()