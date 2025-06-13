import os
import requests
import time

prefixes = ["/usr", "/bin", "/etc", "/var"]

filename = input("Enter temporary file name: ")
folder = os.path.dirname(filename)
if not os.path.exists(folder):
    print("Folder does not exist")
if any([folder.startswith(prefix) for prefix in prefixes]):
    print("Folder is on deny list!")

file = open(filename, "w")

lines = eval(input("Enter the number of urls: "))
timesum = 0
for i in range(lines):
    url = input("Enter url: ")
    
    start = time.time()
    response = requests.get(url)
    end = time.time()

    file.write(str(response.status_code) + "\n")
    timesum += end - start

file.write("Finished in " + str(timesum) + " seconds\n")
file.write("Average time: " + str(timesum / lines) + " seconds\n")
