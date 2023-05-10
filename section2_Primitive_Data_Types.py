# Strings
print("\n______________Strings______________\n")

# Triple quote to write multilines string

message = """
Hello,

This is a multiline string
"""

name = "Python Programming"

# Length of String

print(len(message))
print(len(name))

# Acces specific characters in a string

# First character
print(name[0])

# First Character from the end of the string
print(name[-1])

# First 3 Character from the start of the string
print(name[0:3])

print(name[0:])

print(name[:3])

print(name[:])

######################################################################################

# Escape Sequence
print("\n______________Esccape Sequences______________\n")

# \""
# \\
# \'
# \n -> new Line

course = 'Python "Programming'

print(course)

######################################################################################

first = "Tim"
last = "Horton"

# String Conceatenation

full_name = first + " " + last
print("\n", full_name)

# Formatted String
full = f"{first} {last}"
print('full = f"{first} {last}" : ', full)

full = f"{len(first)} {last}"
print('full = f"{len(first)} {last}" : ', full)

full = f"{first} {2+5}"
print('full = f"{first} {2+5}" : ', full)

######################################################################################

# String Methods
print("\n______________String Methods______________\n")


name = "Python Programming"

# Convert to Upper case [Note: it returns a new string]
print(name.upper())
# PYTHON PROGRAMMING

# Convert to Lower case [Note: it returns a new string]
print(name.lower())
# python programming


# Capitlise first letter of every word [Note: it returns a new string]
name = "python programming lang"
print(name.title())
# Python Programming Lang


# Remove unnecessary white spaces from begining or end of string [Note: it returns a new string]
name = "  python programming lang      "
print(name.strip())
# python programming lang

# Remove unnecessary white spaces from BEGINING of string [Note: it returns a new string]
name = "    python programming lang      "
print(name.lstrip())
# python programming lang

# Remove unnecessary white spaces from  END of string [Note: it returns a new string]
print(name.rstrip())
#    python programming lang


# Find index of a substring
name = "python programming lang"
print(name.find("pro"))
# 7

# Replace a string  with another
name = "python programming lang pylance"
print(name.replace("py", "jy"))
# jython programming lang jylance

# Check for existence of character/string [Note: Difference between in and find() is in gives a boolean,
#  find() gives index]
print("pro" in name)  # This an expression -> Return True False
# True


# Check for non existence of character/string [Note: Difference between in and find() is in gives a boolean,
#  find() gives index]
print("swift" not in name)  # This an expression -> Return True False
# True

########################################---6---##############################################

# Numbers
print("\n______________Numbers______________\n")

# Integer
x = 1

# Float
y = 2.1

# Complex Number
z = 1 + 2j  # a + bi

# Dvision - Regular [Returns float]
print(10 / 2)
# 5.0

# Division - Returns Integer
print(10 // 3)
# 3

# Modulus [Remainder]
print(10 % 3)
# 1

# Exponent [Left to the power right]
print(10**3)
# 1000

x = 10
x = x + 3
x += 3  # Augmented Assignment Operator
######################################---7---################################################

# Number Functions
print("\n______________Number Functions______________\n")

# Rounding a number
print(round(2.9))
# 3

# Absolute value of a numnber
print(abs(-2.9))
# 2.9

# Math Module
import math

# Ceiling of number
print(math.ceil(3.6))
# 4

######################################---8---################################################
# Type Conversion
print("\n______________Type Conversion______________\n")

# To get intput from the user
x = input("x: ")  # Input comes in the form of string
print(type(x))  # Type is function to find the type of a varibale
# x: 9
y = int(x) + 1
print(f"x: {x}, y: {y}")
# x: 9, y: 10

# Falsy - Whenever we use these in boolean contex it will be false, anything else is true
# ""
# 0
# None
