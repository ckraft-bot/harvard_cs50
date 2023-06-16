##------------------------------------- Regular Expression
"""
Learn Regex- how to validate, format inputs, and extract
Regular expression: sequence of characters that specifies a match pattern in text.  
"""
## VALIDATE
# poor validation system 1 - low standards
email_input = input("What's your email address? ").strip()
if "@" in email_input and "." in email_input:
    print("Valid")
else:
    print("Invalid")

# poor validation system 2 - someone can still be malicious and not provide proper email
email_input = input("What's your email address? ").strip() # strip the str input to have username and domain
username, domain = email_input.split("@")

if username and domain.endswith(".com"): # two bools to check if there's a username and a .com somewhere in the email address str
    print("Valid")
else:
    print("Invalid")

# moderate validation system 1 - not the most bullet proof but better than the above 2 examples
import re
email_input = input("What's your email address? ").strip()

"""
.           = any character, 
*           = multiple characters that is zero or greater
+           = at least 1 or more characters
\.          =  match on the single period of ".com" or ".edu"; the backslash just means to take soemthing literally
^           = matches the start of the string
$           = matches the end of the string or just before the new line
[]          = set of characters allowed
[^]         = set of characters not allowed
\w          = alphanumberic and underscore p.s. the long way to write \w is [a-zA-Z0-9_]
A|B         = either a or b
(...)       = group
(?:...)     = non capturing version
?           = something or some group precending the ? can optionally be there or not there

flags built into re()
    - re.IGNORECASE
    - re.MULTILINE
    - re.DOTALL
"""
# >= 1 chars to the left and right of the @ symbol, also need to end in .com
re.search(r"^.+@.+\.com$", email_input)

# >= 1 chars to the left and right of the @ symbol that are acceptable include
    # alphanumeric in strings
    # alphabet casing is accounted for
    # underscores
# a sub domian is allowed with this denotation (\w+\.) after the @ symbol 
# also need to end in .com or .edu or .net or .gov or .org
if re.search(r"^\w+@(\w+\.)?\w\.(com|edu|net|gov|org)$", email_input, re.IGNORECASE): #3rd arg re.IGNORECASE is a flag arguemnt that comes with re.search()
    print("Valid")
    # valid examples: malan@cs50.harvard.edu, malan@harvard.edu
else:
    print("Invalid")
    # invalid examples: malan@@@cs50.harvard.edu, malan@@@@harvard.edu, his email is malan@harvard.edu



## FORMAT AND VALIDATE
# poor format system 1 
name_input = input("What's your name? ").strip() # stripping leading/trailing white spaces

if"," in name_input:
    # particion full name to L, F name
    last, first = name_input.split(", ") # assuming the user adds space after comma
    # overriding the L, F name format
    name_fix = f"{first} {last}"

print(f"hello {name_fix}")

# moderate format system 1 
name_input = input("What's your name? ").strip() # stripping leading/trailing white spaces
matches = re.search(r"^(.+), (.+)$", name_input) 

if matches:
    last, first = matches.groups() # return groups that are captured, to capture you need to group chars by ()
    name_fix = f"{first} {last}"
print(f"hello {name_fix}")

# moderate format system 2
name_input = input("What's your name? ").strip() # stripping leading/trailing white spaces
matches = re.search(r"^(.+), (.+)$", name_input) 

if matches:
    last = matches.group(1) # return a specific group that is captured
    first = matches.group(2)
    name_fix = f"{first} {last}"
print(f"hello {name_fix}")

# moderate format system 3 - compact version of moderate format system 2
name_input = input("What's your name? ").strip() # stripping leading/trailing white spaces
matches = re.search(r"^(.+), *(.+)$", name_input) # the * will help with space toleration in the format stage

if matches:
    name_fix = matches.group(2) + " " + matches.group(1)
print(f"hello {name_fix}")

# moderate format system 4 - compact version of moderate format system 3 
name_input = input("What's your name? ").strip() # stripping leading/trailing white spaces
# ANNOUNCEMENT meet the walrus operator denoted like this :=
    # walrus operator: officially known as the assignment expression operator, it can assign right to left AND evaluate bool
if matches := re.search(r"^(.+), *(.+)$", name_input): # the * will help with space toleration in the format stage
    name_fix = matches.group(2) + " " + matches.group(1)
print(f"hello {name_fix}")



## EXTRACT
# find twitter handle from their twitter url
url = input("URL: ").strip()

# method 1
username = url.removeprefix("https://twitter/")
print(f"Username: {username}")

# method 2 - find and replace
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url) # building lots of tolerance with regex
print(f"Username: {username}")

# method 3 - capture everthing to the right twitter.com/
matches = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE) # building lots of tolerance with regex
if matches:
    print(f"Username:", matches.group(2))

# method 4 - capture everthing to the right twitter.com/ as a walrus
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE): # whether www is in the input or not do not capture it
    print(f"Username:", matches.group(1))
