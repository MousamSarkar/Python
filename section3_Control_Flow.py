######################################################################################

# Access ASCII value

print(ord("A"))
# A-Z :  65-90 and a-z : 97-122
"""
In python logical operators are short-circuit that is in a if statement there are two conditions joined by
an AND operator, it will stop at the first condition if it is false. It will only continue to check the next
condition if the first condition is true."""

#For-Else statement

successful = False
for i in range(3):
    print("P")
    if successful:
        print(successful)
        break
else:
    print("Exit after 3 times")
"""
P
P
P
Exit after 3 times
"""

successful = True
for i in range(3):
    print("P")
    if successful:
        print(successful)
        break
else:
    print("Exit after 3 times")
"""
P
True
"""

for x in "Python":
    print(x)
"""
P
y
t
h
o
n
"""
######################################################################################

# While Loops

number = 100
while number > 0:
    print(number)
    number //= 2

