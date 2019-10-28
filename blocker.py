'''
Administrative privileges required to run the script
> linux:: 
  sudo python3 blocker.py
> windows:
  "Run as administrator" the cmd command to open terminal
  python blocker.py
'''
import time
from datetime import datetime as dt
from sys import platform
from sys import argv

hostsPath=r"C:\Windows\System32\drivers\etc\hosts"
hostsPathTemp=r"C:\\dev\\basics\\hosts"
websitesList = [
    'facebook.com',
    'www.facebook.com',
    'instagram.com',
    'www.instagram.com',
    'digi24.ro',
    'www.digi24.ro',
    'stirileprotv.ro',
    ]
redirect = '127.0.0.1'

# setting the start and end hours during which 
# the websites are in hosts (blocked)
# the blocker will block a list of websites over a time span defined by startWork and endWork
startWork=8
endWork=18

#use sys.argv to read command line arguments to determine time span to block websites
if len(argv) == 3:
    startWork = int(argv[1])
    endWork = int(argv[2])
    print("Working hours set to {} : {}".format(startWork, endWork))
else:
    print("The begining and the end of work hours haven't beend passed through command line arguments\n\n")


if platform.lower().startswith("win"):
    osys="Windows"
    print(osys)
    hostsPath=r"C:\Windows\System32\drivers\etc\hosts"
elif platform.lower() == 'linux':
    hostsPath=r"/etc/hosts"
    osys = platform
else:
    hostsPath=input("Enter hosts file path: ")

print("Runing websites blocker on {} OS. Press Ctrl-C to stop the program" .format(osys))

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day, startWork) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, endWork):
        print("===Working hours {} :: {} [During office hours]===".format(startWork,endWork))
        with open(hostsPath,"r+") as file:
            content=file.read()
            print("Every 5 seconds, if the websites are not in hosts file they will be added ")
            for website in websitesList:
                if website in content:
                    pass
                else:
                    file.write("{} {} \n".format(redirect, website))
            print("Done")
    else:
        with open(hostsPath,"r+") as file:
            content=file.readlines()
            file.seek(0)
            print("Every 5 seconds, if the line contains any of the websites it won't be written in hosts")
            for line in content:
                #write all the lines that do not contain websites from the list
                if not any(website in line for website in websitesList):
                    file.write(line)
            file.truncate()
  
        print("=== Fun hours... Outside office hours {} : {} ===".format(startWork, endWork))
    time.sleep(5)

