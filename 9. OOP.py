##------------------------------------- OOP
"""
Learn how to write code defensively and a new programming paradigm
There are a few paradigms for programming: proceedural, functional, object-oriented.
Functional programming: passing around functions and anonymous functions such as lambda.
Tuple: a collection of values, immutatble (unchangeable)
    A real use case for using tuples over a list would be if you want to program defensively becasue of its immutable nature.
Classes: blueprint for pieces of data or objects, allow you to invent your own data types, have attritubes.
Objects (a.k.a instances): incarnation of the blueprint
Methods: stores instructions on how functions behave. Essentially, functions under the class are considered methods. 
    Examples: __init__, __str__
Class methods: methods that are bound to a class rather than their objects.
Dunder: double underscore pairs, forexample __init__ is read as "dunder dunder init dunder dunder"
Properties: attributes with more defense mechanism put in place
Decorators: functions that modify behaviors of other functions, denoted by @ signs
Inheritance: hierarchical, borrow attributes like methods and properties from another class
Operator overloading: giving extended meaning beton the predefined operational meaning. 
    For example + is primarily used to add two integer, but can also concat strings, and merge two lists.
"""

# method 1 - proceedural 
name = input("Q1- Name: ")
department = input("Q1- Department: ")
print(f"{name} from the {department} department")



# method 2 - better than method 1
def method_2():
    name = get_name()
    department = get_dept()
    print(f"{name} from the {department} department")

def get_name():
    return input("Q2- Name: ")

def get_dept():
    return input("Q2- Department: ")

method_2()



# method 3 - create a tuple and index through it
def method_3():
    employee = get_employee()
    # print the 1st and 2nd locations from the employee tuple
    print(f"{employee[0]} from the {employee[1]} department")
    
def get_employee(): # return multiple values
    name = input("Q3- Name: ")
    department = input("Q3- Department: ")
    # returning a tuple with 
    return (name, department) # = employee

method_3()



# method 4 - create a dictionary and access elements inside it
def method_4():
    employee = get_employee()
    # override user input 's second value
    print(f"{employee['name']} from the {employee['department']} department")
    
def get_employee(): # return multiple values
    employee = {}
    employee["name"] = input("Q4- Name: ")
    employee["department"] = input("Q4- Department: ")
    return employee

method_4()



# method 5 - consolidate method 4
def method_5():
    employee = get_employee()
    # override user input 's second value
    if employee["name"] == "Dwight": # As much as Dwight thinks he's in mangement he's not
        employee["department"] == "Sales" # he's in sales
    print(f"{employee['name']} from the {employee['department']} department")
    
def get_employee(): 
    name = input("Q5- Name: ")
    department = input("Q5- Department: ")
    return{"name " : name, "department": department} # create and return a dicitonary in one line

method_5()



# method 6 - create classes
class Contacts:
    ...
    
def method_6():
    employee = get_employee()
    print(f"{employee.name} from the {employee.department}")

def get_employee(): 
    # instantiate an object
    employee = Contacts() # this line is an object of the class called Contacts as seen in line 85
    employee.name = input("Q6- Name: ") # employee.attribute
    employee.department = input("Q6- Department: ") # employee.attribute
    return employee

method_6()



# method 7 - refine method 6
class Contacts:
    def __init__(self, name, department): # self, parameter 1, parameter 2...
        # objects = instance variables
        self.name = name
        self.department = department
    
def method_7():
    employee = get_employee()
    print(f"{employee.name} from the {employee.department}")

def get_employee(): 
    name = input("Q7- Name: ") # employee.attribute
    department = input("Q7- Department: ") # employee.attribute
    # call Contacts() class as a fucntion and pass in the values name and dept
    employee = Contacts(name, department)
    return employee

method_7()



# method 8 - build validation into objects
class Contacts:
    def __init__(self, name, department): # self, parameter 1, parameter 2...
        if not name:
            # signal an error, create your own error alerts
            raise ValueError("Missing name")
        if department not in ["HR", "Management", "Accounting", "Sales", "Product Oversight", "Warehouse", "Reception"]:
            raise ValueError("Invalid department")
        # objects = instance variables
        self.name = name
        self.department = department
        
    def __str__(self):
        return f"{self.name} from the {self.department}"
    
def method_8():
    employee = get_employee()
    print(employee)

def get_employee(): 
    name = input("Q8- Name: ") # employee.attribute
    department = input("Q8- Department: ") # employee.attribute
    # call Contacts() class as a fucntion and pass in the values name and dept
    return Contacts(name, department)

method_8()



# method 9 - build own methods
class Contacts:
    def __init__(self, name, department, office): # self, parameter 1, parameter 2...
        if not name:
            # signal an error, create your own error alerts
            raise ValueError("Missing name")
        if department not in ["HR", "Management", "Accounting", "Sales", "Product Oversight", "Warehouse", "Reception"]:
            raise ValueError("Invalid department")
        if office not in ["Scranton", "Corporate", "Utica", "Stamford", "Nashua", "Akron", "Albany", "Rochester", "Syracuse"]:
            raise ValueError("Invalid department")
        # objects = instance variables
        self.name = name
        self.department = department
        self.office = office # office branch
        
    def __str__(self):
        return f"{self.name} from the {self.department}"
    
    def spirit(self): # team spirit or unique character of each branch
        match self.office:
            case "Scranton":
                return "Electric city"
            case "Corporate":
                return "Wallace"
            case __annotations_:
                return "Dunder Mifflin"
    
def method_9():
    employee = get_employee()
    print("Team spirit!")
    print(employee.spirit())

def get_employee(): 
    name = input("Q9- Name: ") # employee.attribute
    department = input("Q9- Department: ") # employee.attribute
    office = input("Q9- Office Branch: ") # employee.attribute
    # call Contacts() class as a fucntion and pass in the values name and dept
    return Contacts(name, department, office)

method_9()



# method 10 - add properties -- getter and setter
class Contacts:
    def __init__(self, name, department): # self, parameter 1, parameter 2...
        if not name:
            # signal an error, create your own error alerts
            raise ValueError("Missing name")
        # objects = instance variables
        self.name = name
        self.department = department
        
    def __str__(self):
        return f"{self.name} from the {self.department}"
    
    # getter
    @property
    def name(self):
        return self._name
    
    @name.setter
    #setter
    def name(self, name):
        if not name:
            # signal an error, create your own error alerts
            raise ValueError("Missing name")
        self._name = name

    @property
    # getter
    def department(self):
        return self._department

    @department.setter
    #setter
    def department(self, department):
        if department not in ["HR", "Management", "Accounting", "Sales", "Product Oversight", "Warehouse", "Reception"]:
            raise ValueError("Invalid department")
        self._department = department

def method_10():
    employee = get_employee()
    print(employee)

def get_employee(): 
    name = input("Q10- Name: ") # employee.attribute
    department = input("Q10- Department: ") # employee.attribute
    # call Contacts() class as a fucntion and pass in the values name and dept
    return Contacts(name, department)

method_10()



# method 11a - class method applied to method 10
class Contacts:
    def __init__(self, name, department): # self, parameter 1, parameter 2...
        if not name:
            # signal an error, create your own error alerts
            raise ValueError("Missing name")
        # objects = instance variables
        self.name = name
        self.department = department
        
    def __str__(self):
        return f"{self.name} from the {self.department}"
    
    @classmethod # refined version of the code block in lines 245-249
    def get(cls):
        name = input("Q11- Name: ") # employee.attribute
        department = input("Q11- Department: ") # employee.attribute
        return cls(name, department)
    
def method_11():
    employee = Contacts.get() # instantiate the Contacts object rather than the get_employee function, compare this line to 242
    print(employee)

method_11()



# method 11b - class method
import random
class Chores: # inpsired by the s2 ep 13 of the office called "The Secret"
    room = ["toilet", "break room", "kitchen", "warehosue"]
    
    @classmethod
    def sort(cls, name):
        print(name, "will clean", random.choice(cls.room))

# instantiate an object of a class
Chores.sort("Ryan")




# method 12 - inheritance
class Capitalists:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Employee(Capitalists):
    def __init__(self, name, title):
        # refrencing the super class which in this case is the Capitalists class
        super().__init__(name)
        # employee title
        self.title = title 

class Boss(Capitalists):
    def __init__(self, name, department):
        # referencing the super class which in this case is the Capitalists class
        super().__init__(name)
        # boss dept
        self.department = department

capitalists = Capitalists("Kelly")
employee = Employee("Jim", "Salesman") # name, title
boss = Boss("Michael", "Management") # name, dept



# method 13 - operator overload
class Compensation():
    def __init__(self, base_pay=0, PTO=0, bonus=0):
        self.base_pay = base_pay
        self.PTO = PTO
        self.bonus = bonus
    
    def __str__(self) -> str:
        return f"${self.base_pay} base_pay, {self.PTO} PTO days, ${self.bonus} = bonus"
    
    # overload the operator object.__add__(self,other)
    def __add__(self,other): #(operand on the left, operand on the right) = (Dwight, Jim)
        # adding Dwight and Jim's compensations
        base_pays = self.base_pay + other.base_pay
        PTOs = self.PTO + other.PTO
        bonuses = self.bonus + other.bonus
        return Compensation(base_pays, PTOs, bonuses)

Dwight = Compensation(100,50,25)
print(Dwight)

Jim = Compensation(100,30,20)
print(Jim)

total = Dwight + Jim
print(f"total: {total}")