##------------------------------------- Loops
"""
Learn loops such as: while, for, nested for
Learn data types/functions of data tpyes such as: lists, dict/len()
    len() is used on dtypes like tuple or list
"""

# LOOPS
i = 3
while i != 0:
    print("meow")
    i = i - 1 # counting down

i = 1
while i <= 3:
    print("woof")
    i = i + 1 # counting up

i = 0
while i < 3:
    print("oink")
    i += 1 # counting up

for i in range(10): # range() makes it easier so we don't need to type this out >> [0,1,2...9]
    print("baa")

print("moo\n" * 3, end = "")

while True:
    n = int(input("Type a positive integer: "))
    if n > 0:
        break

for _ in range(n):
    print("ribbit")

def lion_noise():
    number = get_number()
    roar(number)

def get_number():
    while True:
        n = int(input("Type a positive integer: "))
        if n > 0:
            return n

def roar(n):
    for _ in range(n):
        print("roar")

lion_noise()

# LISTS
the_office_cast = ["Michael", "Pam", "Jim", "Dwight", "Angela", "Erin", "Kelly", "Andy", "Ryan", "Stanley", "Toby", "Meredith", "Kevin", "Creed", "Oscar", "Phyllis"]
print(the_office_cast[0:5]) # output: ['Michael', 'Pam', 'Jim', 'Dwight', 'Angela']

# Method A achieves the same as Method B
print("\nMethod A")
for cast_member in the_office_cast:
    print(cast_member)

# Method B achieves the same as Method A
print("\nMethod B")
for i in range(len(the_office_cast)):
    print(the_office_cast[i])

# Method C achieves the same as Method A adn B but now it also adds ranking
print("\nMethod C")
for i in range(len(the_office_cast)):
    # the i in i+1 arg assigns the rank to the items,  +1 in the first argument counts like a human
    print(i+1, the_office_cast[i]) 

# DICT
dunder_mifflin = {"Michael":"Manager", 
            "Pam":"Receptionist", 
            "Jim": "Salesman", 
            "Dwight": "Assistant to the Manager", 
            "Angela": "Accountant"
            }

print("\nLooking up Pam's job")
print(dunder_mifflin["Pam"]) # output: Receptionist

print("\nPrints just the keys in the dict")
for employee in dunder_mifflin:
    print(employee) # prints only the keys

print("\nPrints the keys and values in the dict")
for employee in dunder_mifflin:
    print(employee, dunder_mifflin[employee], sep=" - ") # prints the keys and values

# storing multiple keys and values
dunder_mifflin = [
    {"name": "Michael", "job": "Manger", "sex": "M"},
    {"name": "Pam", "job": "Receptionist", "sex": "F"},
    {"name": "Jim", "job": "Salesman", "sex": "M"},
    {"name": "Dwight", "job": "Assistant to the Manager", "sex": None},
    {"name": "Angela", "job": "Accountant", "sex": "F"}
    ]

print("\nPrints the keys and values in the dict based on selection")
for employee in dunder_mifflin:
    print(employee["name"], employee["job"], employee["sex"], sep=", ") # prints the keys and values

# Mario vertical
def mario_v(): 
    print_column(3)

def print_column(height):
    for _ in range (height):
        print("#\n" * height, end="")
mario_v()

# Mario horizontal
def mario_h(): 
    print_row(5)

def print_row(length):
    print("?" * length)
mario_h()

# Mario 
def mario(): 
    print_square(3)

def print_square(size): # accounting for heigh and length, three rows of bricks and three columns of bricks 3x3
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print brick
            print("#", end="")
        # create new line after a row of 1x3 bricks is done, prepare to stack another row of 1x3 bricks
        print()
mario()

# this achieves the same as the mario() but with less lines of code
def mario_better():
    print_square(3)

def print_square(size): # accounting for heigh and length, three rows of bricks and three columns of bricks 3x3
    for i in range(size):
        print_row(size)

def print_row(length):
    print("#" * length)
mario_better()


