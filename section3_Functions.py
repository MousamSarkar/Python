""" All functions, by default return the object type "None" if there is no return
parameter """


# Multi-variable input to a function

# [In tuples you cannot modify the tuple.]
def multiply(*numbers):  # This is a tuple
    total = 1
    for number in numbers:
        total *= number
        # print(number)
    return total


# print(multiply(2, 3, 4, 5))

# Dictionary stores key value pairs
def save_user(**user):  # This is a dictionary
    print(user["id"])


save_user(id=1, name='John', age=22)


########################################################

# Local Variable and Global Variable

message = "a"  # Global Variable


def greet(name):
    message = "b"  # Local varibale


greet("Mos")
print(message)
# a

message = "a"  # Global Variable


def greetq(name):
    global message  # changing global variable
    """It is bad practice to change global variable in a function
    like this."""
    message = "b"  # Local varibale


greetq("Mos")
print(message)
# b
