##------------------------------------- Unit Tests
"""
Learn corner cases, assert, pytest, packages

Unit testing: is a method for testing software that looks at the smallest testable pieces of code, called units, which are tested for correct operation. 
    By doing unit testing, we can verify that each part of the code, including helper functions that may not be exposed to the user, works correctly and as intended.
packages: multiple modules orangized in a folder
__init__.py: are required to make Python treat directories containing the file as packages. 
    This prevents directories with a common name, such as string, from unintentionally hiding valid modules that occur later on the module search path. 
    In the simplest case, __init__.py can just be an empty file, but it can also execute initialization code for the package or set the __all__ variable.
pytest: 3rd party program that automates testing as long as you write the test.
    In the terminal type pytest <file_name.py> and pytest wil return which tests failed or passed and how long the tests took.
    You can also test multiple test file by typing pytest <folder_name_containing_all_test_files> into the terminal.
"""
import pytest
import sys, os

# PYTEST
# Testing with integers 
def main():
    x = int(3.3) # edge cases could be plugging these values (-1, 0, 3) in for x 
    print("x squared is", square_this(x))

def square_this(n):
    # this return statment is very crucial for pytesting later on!! Without return you will not see the value returned
    return n * n 
main()



def test_positive():
    # corner casees: 2, 3, -2, and 0
    assert square_this(2) == 4
    assert square_this(3) == 9

def test_negative():
    assert square_this(-2) == 4

def test_zero():
    assert square_this(0) == 0

def tset_str():
    # passing a string will raise a TypeError
    with pytest.raises(TypeError):
        square_this("cat")



# Testing with strings
def main():
    name_input = input("What's your name? ")
    print(hello(name_input))

def hello(to="world"):
    return f"hello {to}"
main()



def test_hello_my_input():
    assert hello("Claire") == "hello Claire"

def test_hello_others_input():
    for name_input in ["Garfield", "Odie", "Arlene", "Jon", "Pooky"]:
        assert hello(name_input) == f"hello {name_input}]"

def test_hello_default():
    assert hello() == "hello world"

