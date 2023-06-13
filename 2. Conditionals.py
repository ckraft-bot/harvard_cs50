##------------------------------------- Conditions
"""
Learn logics, comparison, parity
logics: if, elif, if-else, and, or
comaprisons: =, !=,  <=,, >=, <, >, match
parity: +, -, *, /, %
"""

# COMPARISONS
def compare_1():
    x = int(input("Q1: What's x? "))
    y = int(input("Q1: What's y? "))
    if x < y or x > y: # condition
        print("x is not equal to y")
    else:
        print("x is equal to y")
compare_1()

def compare_2():
    x = int(input("Q2: What's x? "))
    y = int(input("Q2: What's y? "))
    if x != y: # condition, more efficient than line 9
        print("x is not equal to y")
    else:
        print("x is equal to y")
compare_2()

def compare_3():
    x = int(input("Q3: What's x? "))
    y = int(input("Q3: What's y? "))
    if x == y: # condition, reverse of compare 2 function
        print("x is equal to y")
    else:
        print("x is not equal to y")
compare_3()

def compare_4():
    score = int(input("Q4: Insert score "))
    if score >= 90 and score <= 100: # condition with conjuction
        print("Grade: A")
    elif score >= 80 and score < 90:
        print("Grade: B")
    elif score >= 70 and score < 80:
        print("Grade: C")
    elif score >= 60 and score < 70:
        print("Grade: D")
    else:
        print("Grade: F")
compare_4()

def compare_5():
    score = int(input("Q5: Insert score "))
    #if 90 <= score and score <= 100: # condition with conjuction, beutify boundaries
    if 90 <= score <= 100: # condition with conjuction, beutify boundaries, cleaned code
        print("Grade: A")
    #elif  80 <= score and score < 90:
    elif  80 <= score < 90:
        print("Grade: B")
    #elif 70 <= score and score < 80:
    elif 70 <= score < 80:
        print("Grade: C")
    #elif 60 <= score and score < 70:
    elif 60 <= score < 70:
        print("Grade: D")
    else:
        print("Grade: F")
compare_5()

def compare_6():
    score = int(input("Q6: Insert score "))
    if score >= 90: # condition can still be written simpler and more optmized
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
compare_6()


# PARITIES
def parity():
    x = int(input("Q7: What's x? "))
    if x % 2 == 0:
        print("Even") # looking at if the remainder is 0 or not to decide if its even or odd
    else:
        print("Odd")
parity()

def parity_better(): 
    x = int(input("Q8: What's x? "))
    if is_even(x): # calling our own custom is_even() inside the parity_better()
        print("Even") # looking at the bool statements in lines 98 and 100 to decide if it's even or odd
    else:
        print("Odd") # looking at the bool statements in lines 98 and 100 to decide if it's even or odd
    
def is_even(n): # python doesn't have an even or odd function so we create a custom function called is_even()
    if n % 2 == 0: # looking at if the remainder is 0 or not to decide if the bool statement is True or False for the is_even()
        return True 
    else:
        return False
parity_better()

def parity_much_better(): 
    x = int(input("Q9: What's x? "))
    if is_even(x): # calling our own custom is_even() inside the parity_better()
        print("Even") # looking at the bool statements in lines 98 and 100 to decide if it's even or odd
    else:
        print("Odd") # looking at the bool statements in lines 98 and 100 to decide if it's even or odd
    
def is_even(n): # python doesn't have an even or odd function so we create a custom function called is_even()
    return True if n % 2 == 0 else False # pythonic way - readable and beutiful code, condensed 4 lines to 1 line (refer to lines 97-100)
parity_much_better()

def parity_elegant(): 
    x = int(input("Q10: What's x? "))
    if is_even(x): # calling our own custom is_even() inside the parity_better()
        print("Even") # looking at the bool statements in lines 98 and 100 to decide if it's even or odd
    else:
        print("Odd") # looking at the bool statements in lines 98 and 100 to decide if it's even or odd
    
def is_even(n): # python doesn't have an even or odd function so we create a custom function called is_even()
    return n % 2 == 0 # elegant version of line 112
parity_elegant()

def owner():
    name_input = input("Q11: What's the name? ") 
    if name_input == "Garfield": # Jon's cat
        print("Owner is: Jon")
    elif name_input == "Odie": # Jon's dog
        print("Owner is: Jon")
    elif name_input == "Herbie": # Jon's frog
        print("Owner is: Jon")
    elif name_input == "Arlene": # Garfield's girlfriend/ pink cat
        print("Owner is: unknown")
    else:
        print("Who?")
owner()

def owner_better():
    name_input = input("Q12: What's the name? ") 
    if name_input == "Garfield" or name_input == "Odie" or name_input == "Herbie": # Jon's cat, dog, frog
        print("Owner is: Jon")
    elif name_input == "Arlene": # Garfield's girlfriend/ pink cat
        print("Owner is: unknown")
    else:
        print("Who?")
owner_better()

def owner_much_better():
    name_input = input("Q13: What's the name? ") 
    match name_input:
        case "Garfield" | "Odie" | "Herbie": # the | signifies or
            print("Owner is: Jon")
        case "Arlene":
            print("Owner is: unknown")
        case _: # the _ is catch all
            print("Who?")
owner_much_better()