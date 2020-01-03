'''
The blocker will block a list of websites over a time span set by
startWork and endWork

Administrative privileges required to run the script
> linux:
sudo python3 blocker.py
  furthermore, to set the time span during which the websites will be blocked,
  the starting time and the ending time can be added as command line arguments
sudo python3 blocker.py 7 19
> windows:
  "Run as administrator" the cmd command to open terminal
python blocker.py
python blocker.py 7 19

[Note] The banlist.conf file should not contain any blank lines
'''

import time
from datetime import datetime as dt
from sys import platform
from sys import argv
from os import path

hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
# default websites list, in case the configuration file is not present

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
sleep_time = 5  # how often the check is performed

# Set the 'hosts' file path depending on the OS
if platform.lower().startswith("win"):
    osys = "Windows"
    print(osys)
    hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
elif platform.lower() == 'linux':
    hostsPath = r"/etc/hosts"
    osys = platform
else:
    hostsPath = input("Enter hosts file path: ")

print(f'Runing blocker on {osys}. Press Ctrl-C to stop the program')
if len(argv) == 3:
    startWork = int(argv[1])
    endWork = int(argv[2])
    print("Working hours set to {} : {}".format(startWork, endWork))
else:
    print('! Default time span {startWork}:{endWork} \n\n')

# Reading the list of websites from a configuration file
if path.exists(sourceList):
    print('Reading the list of websites from {} file'.format(sourceList))
    with open(sourceList) as f:
        websitesL = f.read().splitlines()
        print(f'Websites banned during the time span {startWork} - {endWork}')
        for website in websitesL:
            print(website)
        websitesList = websitesL

while True:
    start_time = dt(dt.now().year, dt.now().month, dt.now().day, startWork)
    end_time = dt(dt.now().year, dt.now().month, dt.now().day, endWork)
    if start_time < dt.now() < end_time:
        print(f'=== Working hours {startWork} :: {endWork} ===')
        with open(hostsPath, "r+") as file:
            content = file.read()
            print(f'Every {sleep_time} update the {hostsPath}')
            for website in websitesList:
                if website in content:
                    pass
                else:
                    file.write(f'{redirect} {website}\n')
            print("Update completed! ")
    else:
        print(f'Fun hours... Outside office hours {startWork} : {endWork}')
        with open(hostsPath, "r+") as file:
            content_lines = file.readlines()
            file.seek(0)
            print(
                f'Every {sleep_time} seconds, if the line contains any '
                'of the websites it won\'t be written in hosts'
                )
            for line in content_lines:
                if not any(website in line for website in websitesList):
                    file.write(line)
            file.truncate()
    time.sleep(sleep_time)
