##------------------------------------- File I/O
"""
Learn how to read from & write to operations; list; open(); lambda; txt, csv; PIL (a.k.a. 'pillow')

File IO: input and output of files
Lambda: a small anonymous function, can take any number of arguments or paraments, but can only have one expression.
PIL: allow you to navigate images
"""

## STORED ONLY IN MEMORY
names = []

for _ in range(3):
    name_input = input("What's your name? ") 
    names.append(name_input)

for name_input in sorted(names):
    print(f"hello {name_input}") # just stored in the memory, as soon as the program exits the data is lost



## WRITE TO FILE
# text files
#file = open("names.txt", "w")  create a file with write privilges so it can be modified later

# If you change the 2nd argument to "a" then you can run this file ,"7. File IO.py", repeatedly and respond to the What's your name? prompt.
# Each response to the prompt that input is recorded in your names.txt.
with open("names.txt", "a") as file:
    # The \n is to escape the lines of names given in each prompt to prevent the names from being stored in a squished format in the names.txt/
    # Each name has it's own line.
    file.write(f"{name_input}\n") 

file.close()


# csv files
import csv
character_input = input("Tell me a character you like in The Office show: ")
department_input = input("Give me a department name in The Office show: ")

with open("the_office_roster", "a") as file:
    writer = csv.writer(file, fieldnames=["employee", "department"])
    writer.writerow({"employee": character_input,
                    "department": department_input})


## READ FROM FILE
# text files - ok design
with open("names.txt", "r") as file:
    # read all the lines in the file and 
    lines = file.readlines()

for line in lines:
    print("hello", line.rstrip()) #rstrip will strip the extra spaces after the names that are stored in the names.txt

# text files - not a bad design
fruits = []
with open("grocery_list.txt") as file:
    # read all the lines in the file and 
    for line in file:
        fruits.append(line.rstrip())

for fruit in sorted(fruits):
    print(f"buy {fruit}")

# text files - better design
with open("grocery_list.txt") as file:
    # read all the lines in the file
    for line in sorted(file):
        print(f"buy", line.rstrip())

# text files - best design
with open("names.txt", "r") as file:
    # read all the lines in the file and 
    for line in file:
        print("hello", line.rstrip()) #rstrip will strip the extra spaces after the names that are stored in the names.txt



# csv files - good desing
with open("foods.csv") as file:
    # read all the lines in the file 
    for line in file:
        row = line.rstrip().split(",") # strawberry, fruit
        print(f"{row[0]} is {row[1]}") # {} is {} = stawberry is fruit

# csv files - better design
foods = []

with open("foods.csv") as file:
    # read all the lines in the file 
    for line in file:
        food, category = line.rstrip().split(",") # strawberry, fruit
        foods.append(f"{food} is {category}")

for food in sorted(foods):
    print(food) # {} is {} = stawberry is fruit

# csv files - even better design
foods = []

with open("foods.csv") as file:
    # read all the lines in the file 
    for line in file:
        food, category = line.rstrip().split(",") # strawberry, fruit
        food = {} # empty dictionary that will soon hold food and category
        food["food"] = food # storing col 1 in the food{}
        food["category"] = category # storing col 2 in the food{}
        foods.append(food) 

for food in sorted(foods):
    print(f"{food['food']} is categorized as {food['category']}.") # {} is {} = stawberry is categorized as fruit

# csv files - even better design
foods = []

with open("foods.csv") as file:
    # read all the lines in the file 
    for line in file:
        food, category = line.rstrip().split(",") # strawberry, fruit
        food = {"food": food, "category" : category} # dictionary assigned keys
        foods.append(food) 

def get_food(food):
    return food['food']

def get_category(category):
    return food['category']

for food in sorted(foods, key=get_food): # the 2nd arg key= is saying sort based on the food item which is column 1 of csv or 1st key of the dict
    print(f"{food['food']} is categorized as {food['category']}.") # {} is {} = stawberry is categorized as fruit

# csv files - best design
foods = []

with open("foods.csv") as file:
    # read all the lines in the file 
    for line in file:
        food, category = line.rstrip().split(",") # strawberry, fruit
        food = {"food": food, "category": category} # dictionary assigned keys
        foods.append(food) 

# key=lambda food: food["food"] is better than key=get_food that calls a function called get_food()
for food in sorted(foods, key=lambda food: food["food"]): # the 2nd arg key= is saying sort based on the food item which is column 1 of csv or 1st key of the dict
    print(f"{food['food']} is categorized as {food['category']}.") # {} is {} = stawberry is categorized as fruit

# csv files - don't reinvent the wheel
import csv

foods = []

with open("foods.csv") as file:
    reader = csv.reader(file) # reading list of lines in csv
    for row in reader: 
        foods.append({"food": row[0], "category": row[1]})

for food in sorted(foods, key=lambda food: food["food"]): # the 2nd arg key= is saying sort based on the food item which is column 1 of csv or 1st key of the dict
    print(f"{food['food']} is categorized as {food['category']}.") # {} is {} = stawberry is categorized as fruit

# csv files - don't reinvent the wheel, more compact code
foods = []

with open("foods.csv") as file:
    reader = csv.reader(file) # reading list of lines in csv
    for food, category in reader: 
        foods.append({"food": food, "category": category})

for food in sorted(foods, key=lambda food: food["food"]): # the 2nd arg key= is saying sort based on the food item which is column 1 of csv or 1st key of the dict
    print(f"{food['food']} is categorized as {food['category']}.") # {} is {} = stawberry is categorized as fruit

# csv files - don't reinvent the wheel, defensivly coded
foods = []

with open("foods.csv") as file:
    # in short DictReader is better than reader when reading in from csv files
    reader = csv.DictReader(file) # reading dictionaries of lines in csv
    for row in reader: 
        foods.append({"food": row['food'], "category": row['category']}) # does not matter if someone swaps the columns around bc we're reading from the dict

for food in sorted(foods, key=lambda food: food["food"]): # the 2nd arg key= is saying sort based on the food item which is column 1 of csv or 1st key of the dict
    print(f"{food['food']} is categorized as {food['category']}.") # {} is {} = stawberry is categorized as fruit



## Create a gif
import sys
from PIL import Image

images = []

for arg in sys.argv[1:]: # slicing
    image = Image.open(arg)
    images.append(image)

# save to
image[0].save("cat_final.gif", save_all=True, append_images=[images[1]], duration=200, loop=0) # 200 milisecon, loop