##------------------------------------- Libraries
"""
Learn modules, import, from, command-line arguments, slices, packages, pip, APIs, requests, JSON
    Modules: contain functions, classes, and variables
        ex: random, statistics, sys, 
    Import: load in modules
    From: importing functions from a module
    CL arguements: simply anything the user enters after the executable name
        ex: python file_name.py Claire
"""

# RANDOM MODULE
import random # technically importing everything in the random module
## simulates coin flip
coin_flip = random.choice(["heads", "tails"])
print(coin_flip)

## pet preference debate
from random import choice # importing just the ONE specific function, choice, in the random module
pet_preference = choice(["cat", "dog"]) # notice how it's not necessary to type random.choice()?
print(pet_preference)

## random number picker between 1 and 10
random_number = random.randint(1,10)
print(random_number)

## card shuffling
cards = ["jack", "queen", "king", "ace"]
random.shuffle(cards)
for card in cards:
    print(card)



# STATISTICS MODULE
import statistics as stats
print(stats.mean([100, 90]))

# SYS MODULE
import sys
"""
COMMAND-LINE ARGUMENTS
argv = argument vector
if sys.argv[0] then the terminal will output 
    hello, my name is 5. Libraries.py

if sys.argv[1] then the terminal will the second element which is the name you provide after python file_name.py
1. in the terminal if I type ... then the ouput will be hello, my name is Claire.
    python file_name.py Claire 
    Python "5. Libraries.py" Claire
2. in the terminal if I type ... then the output will be IndexError: list index out of range.
    Python "5. Libraries.py" 
"""
print("hello, my name is", sys.argv[0]) 




## design a checking mechanism
# checking if the arguments are over or under the threshold of 2
if len(sys.argv) < 2: 
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])



## single name tag
# checking for errors
if len(sys.argv) < 2: 
    # exits gracefully, because there are too few arguments given, and prints Too few arguments
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    # exits gracefully because there are too many arguments given, and prints Too many arguments
    print("Too many arguments")

# print a single name tag
print("hello, my name is", sys.argv[1])



## multiple name tags
# checking for errors
if len(sys.argv) < 2: 
    # exit gracefully because there are too few arguments given
    sys.exit("Too few arguments")

# print multiple name tags
for arg in sys.argv:
    print("hello, my name is", arg) 
    """
    mini problem on line 83: this will print the first arg, in addition, to the other args you gave like so
        hello, my name is 5. Libraries.py
        hello, my name is Claire
        hello, my name is Garfield
        hello, my name is Link
        hello, my name is Stella
    which includes the file name.
    We only want the args you gave.
    To fix this we can just take a subset of the arguments passed in by using slices
    """



# print multiple name tags refined
# checking for errors
if len(sys.argv) < 2: 
    # exit gracefully because there are too few arguments given
    sys.exit("Too few arguments")

# print multiple name tags
for arg in sys.argv[1:]: # the fix is herr where we specify the index begins at 1 instead of 0
    print("hello, my name is", arg) 
    """
    To fix the issue with index we can just take a subset of the arguments passed in by using slices.
    Indeed slicing resolves the issue. The ouputs look like this.
        hello, my name is Claire
        hello, my name is Garfield
        hello, my name is Link
        hello, my name is Stella
    """



# PACKAGE
# pip install cowsay https://pypi.org/project/cowsay/
## cow
import cowsay 
if len(sys.argv) == 2:
    cowsay.cow("hello " + sys.argv[1])

"""
The cute ouput says this
  ____________
| hello Claire |
  ============
            \
             \
               ^__^
               (oo)\_______
               (__)\       )\/\
                   ||----w |
                   ||     ||
"""



## trex
print(cowsay.trex("hello Claire"))
'''
The cute ouput says this
  ____________
| hello Claire |
  ============
                   \
                    \
                     \
                      \
                         .-=-==--==--.
                   ..-=="  ,'o`)      `.
                 ,'         `"'         \
                :  (                     `.__...._
                |                  )    /         `-=-.
                :       ,vv.-._   /    /               `---==-._
                 \/\/\/VV ^ d88`;'    /                         `.
                     ``  ^/d88P!'    /             ,              `._
                        ^/    !'   ,.      ,      /                  "-,,__,,--'""""-.
                       ^/    !'  ,'  \ . .(      (         _           )  ) ) ) ))_,-.\
                      ^(__ ,!',"'   ;:+.:%:a.     \:.. . ,'          )  )  ) ) ,"'    '
                      ',,,'','     /o:::":%:%a.    \:.:.:         .    )  ) _,'
                       """'       ;':::'' `+%%%a._  \%:%|         ;.). _,-""
                              ,-='_.-'      ``:%::)  )%:|        /:._,"
                             (/(/"           ," ,'_,'%%%:       (_,'
                                            (  (//(`.___;        \
                                             \     \    `         `
                                              `.    `.   `.        :
                                                \. . .\    : . . . :
                                                 \. . .:    `.. . .:
                                                  `..:.:\     \:...\
                                                   ;:.:.;      ::...:
                                                   ):%::       :::::;
                                               __,::%:(        :::::
                                            ,;:%%%%%%%:        ;:%::
                                              ;,--""-.`\  ,=--':%:%:\
                                             /"       "| /-".:%%%%%%%\
                                                             ;,-"'`)%%)
                                                            /"      "|
'''


### APIs
# search songs on itunes
import requests
import json
# after limit= you can change the number to expand or shrink your search results
# after term= you can search for another artist
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=swift") 
# print all info about that one T Swift song
print(json.dumps(response.json()))
"""
The output returns:

{"resultCount":1,"results":[{"wrapperType":"track","kind":"song","artistId":216425159, ... "isStreamable":true}]}
"""

track_name = response.json()
for result in track_name["results"]:
    # print a specific piece of info about that one T Swift song
    print(result["trackName"])
"""
The ouput returns: 

Two Is Better Than One (feat. Taylor Swift)
"""
# hello
from greetings import hello # importing my own package called greetings and function called hello
if len(sys.argv)  == 2: # in the terminal i'm typing python "5. Libraries.py" Claire
    hello(sys.argv[1]) # terminal spits out hello Claire

# goodbye
from greetings import goodbye # importing my own package called greetings and function called hello
if len(sys.argv)  == 2: # in the terminal i'm typing python "5. Libraries.py" Claire
    goodbye(sys.argv[1]) # terminal spits out goodbye Claire