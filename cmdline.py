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

x=4
cond1 = x>0
cond2 = x<20
if cond1 and cond2:
    print ("x")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)
print(type(x))
print("Key: Value elements of dict.items()")

"""
for key in a_dict.keys():
    print(key, '->', a_dict[key])
"""
print("Using dictionary name")
for key in car:
    print("{}:{}".format(key,car[key]))

for item in car.items():
    print(item)
print("\nUsing .items()")
for key, val in car.items():
    print(key,val)

tuples=(1,4,5)
for i in tuples:
    print(i)

myL=[4,5,8,9,0]

newL=[item for item in myL if item>5]
print(newL)
#for item in myL if item > 7:
 #   print(item)
my_movies = [['How I Met Your Mother', 'Friends', 'Silicon Valley'],
    ['Family Guy', 'South Park', 'Rick and Morty'],
    ['Breaking Bad', 'Game of Thrones', 'The Wire']]
#"The title [movie_title] is [X] characters long."

for movieL in my_movies:
    for movie in movieL:
        print ("The title {} is {} characters long".format(movie, len(movie)))

for i in range(1,3):
    print(i)


down = 0
up = 100
print('a')
for i in range(1,10):
    guessed = int((up + down) / 2)
    answer=''
    '''
    while True:
        answer = input('Are you {} years old ? [less / more / correct] '.format(guessed))
        if answer in ['less','correct','more']:
            break   
    
    '''
    while answer not in ['less','correct','more']:
        answer = input('Are you {} years old ? [less / more / correct] '.format(guessed))
    if answer == 'correct':
        print ('Nice, so your age is {} '.format(guessed))
        break
    elif answer =='less':
        up = guessed
    else:
        down = guessed
    

