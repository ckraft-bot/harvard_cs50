##------------------------------------- Functions & Variables
"""
Learn how to create a function, custom default parameter(s), pass in variables to the function
"""

def main():
# GREETING - working with str
    name_input = input("What's your name? ") # varaiables are done with a single equal sign, "=" means assignemnt. "==" is for vlaue equity.
    greeting(name_input) # output baaed on the user input variable, name_input is the arguement

def greeting(to="everyone"): # default paramenter will be "everyooe" if no input is given to the variable name_input, you can customize parameters.
    print("hello", to) # to is the arguemtn in this print statment
greeting() # default output will be "hello"everyone" for this function

# SQUARE ROOT - working with int
def square(n):
    return n * n # return is a statement that will return the value back to the caller. If you input 2 then it will return 2. In this case my input for n is 2, n*n or 2*2 should be 4.
    #return pow(n, 2) # this is another way to write n*n using Python's built in pow()

def calc():
    x = int(input("what's x? "))
    print("x squared is", square(x))
calc()

main() # calling the main function will go in order of running each function and arguements