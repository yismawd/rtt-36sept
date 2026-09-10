
# Into to Python (Redux)

# Single Line Comment - inline comment

'''
MultiLine Comment / Document Comments

Python is read top --> bottom, left to right - sequencing

loosely typed - we do not declare datatypes
'''

# To Run Python: python3 <name of file>

print('Hello, World!')

"""
Variable - container with a label on it. You can put ANY information inside you want and you use the name to grab that value/info
Box with a label

Naming conventions for variables:
- Cannot START with a number
- Cannot include spaces
- Cannot include most symbols (can use underscore)
- Should be as clear as necessary
- Cannot use reserved keywords
- Case-sensitive
- Must start with a letter or underscore
- Insdustry Standard: use snake_case or camelCase.
"""

# Primitive Data Types

# Number:
# int - integers. whole numbers. Discrete values.
# float - floating point decimal numbers.
fav_number = 13

# Strings - text, ALWAYS surrounded with quotes. Double or single quotes.
name = 'Dylan'
cat_name = "Thumbs"
text = "Joey says, \"HelloWorld\", when he greets the day"

# Boolean - bools. True/False. 0,1.
# Do not put quotes on a boolean, you will make a string, and all populated string are True
speak_french = False
speak_english = True

print(name, "favorite number", fav_number)
# Formatted strings (f-string) allow the direct injection of variables/values into a string.
# Use f'' to declare a string type, then curly braces {} to surround the dynamic values (variables)
print(f'{name} has a pet named {cat_name}')


# input() function - accepts input from the user in the terminal. To call (invoke, run) a function you use parenthases
name = input("What is your name? ")
print(f'Hello {name}')
age = input('How old are you? ')
print(f'You are {age} years old!')