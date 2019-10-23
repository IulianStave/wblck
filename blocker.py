import time
from datetime import datetime as dt
from sys import platform

hostsPath='C:\Windows\System32\drivers\etc\hosts'
hostsPathTemp="C:\\dev\\basics\\hosts"
websitesList = ['facebook.com','www.facebook.com','instagram.com','www.instagram.com']
redirect = '127.0.0.1'

# setting the start and end hours during which 
# the websites are in hosts (blocked)

startWork=8
endWork=16

#print(hostsPath)
print(platform)
if platform.lower().startswith("win"):
    osys="Windows"
elif platform==platform
print(platform)
#betwwen 8 and 16 the blocker will block a list of websites
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

#file.seek(0)
#print(file.read())