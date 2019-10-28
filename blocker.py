import time
from datetime import datetime as dt
from sys import platform

hostsPath=r"C:\Windows\System32\drivers\etc\hosts"
hostsPathTemp=r"C:\\dev\\basics\\hosts"
websitesList = ['facebook.com','www.facebook.com','instagram.com','www.instagram.com']
redirect = '127.0.0.1'

# setting the start and end hours during which 
# the websites are in hosts (blocked)
# the blocker will block a list of websites over a time span defined by startWork and endWork
startWork=8
endWork=16


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
        print("===Working hours ===")
        with open(hostsPath,"r+") as file:
            content=file.read()
            #print(content)
            for website in websitesList:
                if website in content:
                    pass
                else:
                    file.write("{} {} \n".format(redirect, website))
    else:
        with open(hostsPath,"r+") as file:
            content=file.readlines()
            file.seek(0)


            for line in content:
                #write all the lines that do not contain websites from the list
                if not any(website in line for website in websitesList):
                    file.write(line)
            file.truncate()


        
        print("Fun hours...")
    time.sleep(5)

