##------------------------------------- Exceptions
"""
Learn SyntaxError, ValueError, NameError
Learn try except, try except else, while true, break, pass
"""

# TRY EXCEPT
try: # best practice: keep the lines of code under try minimal
    x = int(input("Q1: Type a number: "))
    print(f"You typed {x}.")
except ValueError:
    print("What you typed is not a number.")

# TRY EXCEPT ELSE
try:
    pass
    # Some Code.... 
except:
    pass
    # optional block
    # handling of exception (if required)
else:
    pass
    # execute if no exception

try: # best practice: keep the lines of code under try minimal
    x = int(input("Q2: Type a number: "))
except ValueError:
    print("What you typed is not a number.")
else:
    print(f"You typed {x}.") # notice how the print() is now under else: rather than nested under try:?

# TRY EXCEPT ELSE WRAPPED IN WHILE TRUE
# This while True loop will continue to loop through the try loop until it's satisfied with user input as prompted by variable x.
while True:
    try: # best practice: keep the lines of code under try: minimal
        x = int(input("Q3: Type a number: "))
    except ValueError:
        print("What you typed is not a number.")
    else: # this is associated with the try: and not except:
        # once the try loop is satisfied with user input as prompted by variable x it breaks out of the try loop
        break #
# once it breaks out of the try loop it prints
print(f"You typed {x}.") # notice how the print() is now outside of the try loop?

# test4() achieves the same as lines 34 - 43 but a bit cleaned up
def test4():
    x = get_int()
    print(f"x is {x}.")

def get_int():
    while True:
        try: # best practice: keep the lines of code under try: minimal
            x = int(input("Q4: Type a number: "))
        except ValueError:
            print("What you typed is not a number.")
        else:
            return x # Return is stronger than break, it'll break you out of the loop and retun the value. 2-in-1 action
test4()

# test5() achieves the same as test4() but more compact
def test5():
    x = get_int()
    print(f"x is {x}.")

def get_int():
    while True:
        try: # best practice: keep the lines of code under try: minimal
            return int(input("Q5: Type a number: "))
        except ValueError:
            print("What you typed is not a number.")
test5()

# test6() achieves the same as test5() but is passing in the except to gracefully handle the ValueError
def test6():
    x = get_int()
    print(f"x is {x}.")

def get_int():
    while True:
        try: # best practice: keep the lines of code under try: minimal
            return int(input("Q6: Type a number: "))
        except ValueError:
            pass # gracefully handle the ValueError by not printing "What you typed is not a number." repeatedly.
test6()

# test7() achieves the same as test5() but is more refined
def test7():
    x = get_int("Q7: Type a number:  ") # the prompt is now up here under caller func rather than the call-y func
    print(f"x is {x}.")

def get_int(prompt): # this get_int() is more dynamic than the get_int() in test6()
    while True:
        try: # best practice: keep the lines of code under try: minimal
            return int(input(prompt))
        except ValueError:
            pass # gracefully handle the ValueError by not printing "What you typed is not a number." repeatedly.
test7()

