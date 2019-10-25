#Command Line arguments sys.argv
import sys
argumentsCount=len(sys.argv)
script=sys.argv[0]
if argumentsCount>1:
    print("{} arguments passed on command line".format(argumentsCount))
    print("The first argument is always the python script that you ran in command line: \'{}\'".format(script))
    print("Here is the list of command line arguments:")
    print(str(sys.argv))
    #print(type(sys.argv))
    for argument in sys.argv[1:]:
        print(argument)
else:
    print("No arguments passed through command line")
