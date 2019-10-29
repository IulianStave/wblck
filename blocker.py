'''
The blocker will block a list of websites over a time span set by startWork and endWork

Administrative privileges required to run the script
> linux:: 
sudo python3 blocker.py
  furthermore, to set the time span during which the websites will be blocked, 
  the starting time and the ending time can be added as command line arguments
sudo python3 blocker.py 7 19
> windows:
  "Run as administrator" the cmd command to open terminal
python blocker.py
python blocker.py 7 19
'''
import time
from datetime import datetime as dt
from sys import platform
from sys import argv
from os import path

hostsPath=r"C:\Windows\System32\drivers\etc\hosts"
#default websites list, in case the configuration file is not present
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
sourceList = 'banlist.conf'
startWork = 8
endWork = 19
sleep_time = 5 # how often the check is performed

#Set the 'hosts' file path depending on the OS
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

# use sys.argv to read command line arguments to determine time span to block websites
# setting the start and end hours during which
if len(argv) == 3:
    startWork = int(argv[1])
    endWork = int(argv[2])
    print("Working hours set to {} : {}".format(startWork, endWork))
else:
    print("! The begining and the end of work hours haven't beend passed through command line arguments\n\n")

# Reading the list of websites from a configuration file
if path.exists(sourceList):
    print('Reading the list of websites from {} file'.format(sourceList))
    with open(sourceList,"r") as f:
        websitesL = f.read().splitlines()
        print (type(websitesL))
        print("The following websites are banned during the time span {} - {}".format(startWork, endWork))
        for w in websitesL:
            print(w)
        websitesList = websitesL

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day, startWork) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, endWork):
        print("=== Working hours {} :: {} ===".format(startWork,endWork))
        with open(hostsPath,"r+") as file:
            content=file.read()
            print("Every {} seconds, if the websites are not in the hosts file, they will be added to the file".format(sleep_time))
            for website in websitesList:
                if website in content:
                    pass
                else:
                    file.write("{} {} \n".format(redirect, website))
            print("Done")
    else:
        print("=== Fun hours... Outside office hours {} : {} ===".format(startWork, endWork))
        print(websitesList)
        with open(hostsPath,"r+") as file:
            content=file.readlines()
            file.seek(0)
            #print(content)
            print("Every 5 seconds, if the line contains any of the websites it won't be written in hosts")
            for line in content:
                print("===",line)
                #write all the lines that do not contain websites from the list
                if not any(website in line for website in websitesList):
                    file.write(line)
            file.truncate()
    time.sleep(sleep_time)

    '''
    else:
        with open(hostsPath,"r+") as file:
            content = file.readlines()
            file.seek(0)
            print("Every {} seconds, if the line contains any of the websites it won't be written in hosts".format(sleep_time))
            print (content)
            for line in content:
                if not any(website in line for website in websitesList):
                    file.write(line)
            file.truncate()
            print("=== Fun hours, outside working hours {} :: {} ===".format(startWork,endWork))
            print("Done")
  '''

