import os
import requests
import pathlib

prefixes = ["/usr", "/bin", "/etc", "/var", "/tmp"]

filename = input("Enter temporary file name: ")
filename = pathlib.Path(filename).resolve().as_posix()
folder = os.path.dirname(filename)
if not os.path.exists(folder):
    print("Folder does not exist")
    exit(-1)
if any([folder.startswith(prefix) for prefix in prefixes]):
    print("Folder is on deny list!")
    exit(-1)

url = input("Enter URL: ")
res = requests.get(url)
if res.status_code != 200:
    print("Error downloading file")
    exit(-1)

with open(filename, "wb") as f:
    f.write(res.content)

print("File downloaded successfully")
