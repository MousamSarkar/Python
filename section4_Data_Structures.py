from sys import getsizeof
from array import array
from collections import deque


# Lists

# 1-D Lists

letters = ["a", "b", "c"]

# 2-D Lists
matrix = [[0, 1], [2, 3]]

# Multiplying a list

zeros = [1]*5
print(zeros)
# [1, 1, 1, 1, 1]

# List concatenation
combined = zeros + letters
print(combined)
# [1, 1, 1, 1, 1, 'a', 'b', 'c']

# Genrating a list of numbers from 0-20
numbers = list(range(20))
print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

chars = list("Hello World")
print(chars)
# ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

#################################################################################
# Accessing a list elements
print("________________________Accessing a list elements___________________")


letters = ["a", "b", "c", "d"]
print(letters[0])
# a

print(letters[-1])
# d

# Modify lists
letters[0] = "A"
print(letters)
# ['A', 'b', 'c', 'd']

# Getting list of only n elements
print(letters[0:2])
# ['A', 'b']

# Getting list of every alternate values
numbers = list(range(20))
print(numbers[::2])
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Printing list in reverse order
print(numbers[::-1])
# [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#################################################################################
# Unpacking a list
print("________________________Unpacking a list___________________")

numbers = [1, 2, 3]

first = numbers[0]
second = numbers[1]
third = numbers[2]

# Unpacking a list - It is same as the above statements
first, second, third = numbers
"""[Number of elements on the left should be equal to
the number of elements of the list]"""
print(first)
# 1

numbers = [1, 2, 3, 4, 4, 4, 4, 9]

# Unpacking and packing list - *others - packs all other elements
first, second, *other = numbers
print(first)
print(other)
# 1
# [3, 4, 4, 4, 4, 9]

first, *other, last = numbers
print(first, last)
print(other)
# 1 9
# [2, 3, 4, 4, 4, 4]
#################################################################################
# Itterate over List
print("________________________Itterate over List___________________")
letters = ["a", "b", "c"]

for letter in letters:
    print(letter)
"""
a
b
c
"""

# Using enumerate function to get the list and their indexes
for letter in enumerate(letters):
    print(letter)
"""
(0, 'a')
(1, 'b')
(2, 'c')
"""

# Upacking a list
for index, letter in enumerate(letters):
    print(index, letter)
"""
0 a
1 b
2 c
"""
#################################################################################
# Finding in List
print("________________________Finding in List___________________")

letters = ["a", "b", "c"]

print(letters.index("a"))
# 0

if "d" in letters:
    print(letters.index("d"))
# No output as d is not present. Without the if statement, it would give an error

print(letters.count("d"))
# 0 -> Because no element exist
#################################################################################
# Sorting in list
print("________________________Sorting in list___________________")

number = [3, 51, 2, 8, 6]

# Sorting in descending order
number.sort(reverse=True)
print(number)
# [51, 8, 6, 3, 2]

new_number = sorted(number)
print(new_number)
# [2, 3, 6, 8, 51]

new_number = sorted(number, reverse=True)
print(new_number)
# [51, 8, 6, 3, 2]

# Sorting a tuple. Tuples are not iterable directly
items = [
    ("product", 10),
    ("product2", 9),
    ("product3", 12)
]

# If we try to sort the tuples directly, it won't work


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
# [('product2', 9), ('product', 10), ('product3', 12)]
#################################################################################

# Lambda function
print("________________________Lambda function___________________\n")

# This is tuple and hence not iterable directly.
items = [
    ("product", 10),
    ("product2", 9),
    ("product3", 12)
]

# def sort_item(item):
#     return item[1]

# lambda parametes: expression
items.sort(key=lambda item: item[1])
print(items)
# [('product2', 9), ('product', 10), ('product3', 12)].

#################################################################################

# Map function
print("________________________Map function___________________\n")

items = [
    ("product", 10),
    ("product2", 9),
    ("product3", 12)
]

prices = []

# Appending elements from a tuple to a list
for item in items:
    prices.append(item[1])

print(prices)
# [10, 9, 12]

# Mapping values from a function to a iterable
x = map(lambda item: item[1], items)

for item in x:
    print(item)
"""
10
9
12
"""

# Converting a map to a list
x = list(map(lambda item: item[1], items))
print(x)
# [10, 9, 12]

#################################################################################

# Filter function
print("________________________Filter function___________________\n")

items = [
    ("product", 10),
    ("product2", 9),
    ("product3", 12)
]

# We want to get products whose prices are >=10
x = filter(lambda item: item[1] >= 10, items)
print(x)
# <filter object at 0x000001A41C56BAF0>

# converting filter object to list
x = list(filter(lambda item: item[1] >= 10, items))
print(x)
# [('product', 10), ('product3', 12)]

#################################################################################

# List Comprehension
print("________________________List Comprehension___________________\n")


items = [
    ("product", 10),
    ("product2", 9),
    ("product3", 12)
]

prices = list(map(lambda item: item[1], items))

# [expression for item in items] Does the same task as map function
prices = [item[1] for item in items]

filtered = list(filter(lambda item: item[1] >= 10, items))

# filtered =[expression for item in items] Does the same task as filter function
filtered = [item for item in items if item[1] >= 10]


#################################################################################

# Zip Function
print("________________________Zip Function___________________\n")

list1 = [1, 2, 3]
list2 = [10, 20, 30]

# We want to create a tuple from these two lists like [(1,10)]
print(zip(list1, list2))
# <zip object at 0x000002B6D92FFB80>

print(list(zip(list1, list2)))
# [(1, 10), (2, 20), (3, 30)]

print(list(zip("abc", list1, list2)))
# [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]

#################################################################################

# Stack - LIFO
print("________________________Stack___________________\n")

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print(browsing_session)
# [1, 2, 3]

# Deleting the last value in the stack
last = browsing_session.pop()
print(last)
# 3

print(browsing_session)
# [1, 2]

# Checking if the stack is empty or not. If empty, not browsing_session will return true.
if not browsing_session:
    # Printig the last value on the stack
    print("redict", browsing_session[-1])
    # 2

#################################################################################


# Queues - FIFO
print("________________________Queues___________________\n")

# from collections import deque
# From collections module we import deque

# Declaring an empty queue
queue = deque([])

# Adding values to queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# Removes element from the begining of the queue
queue.popleft()
print(queue)
# deque([2, 3, 4])

# Removes element from the end of the queue
queue.pop()
print(queue)
# deque([2, 3])


if not queue:
    print("Empty")

#################################################################################


# Tuples - These are read only lists
print("________________________Tuples___________________\n")

# Defining a tuple
point = 1, 2
point = (1, 2)

# Adding tuples
point = (1, 2) + (3, 4)
print(point)
# (1, 2, 3, 4)

# Multiplying tuples to get same value several times
point = (1, 2) * 3
print(point)
# (1, 2, 1, 2, 1, 2)

# Converting list to a tuple
point = tuple([1, 2])
print(point)
# (1, 2)

# Converting string to a tuple
point = tuple("Hello World")
print(point)
# ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')

point = (1, 2, 3)
print(point[0])
# 1

# Accessing a subpart of the tuple
print(point[0:3])

# Unpacking a tuple
x, y, z = point

# Checking if any value is present or not
if 3 in point:
    print("exists")


#################################################################################


# Swapping Varibales
print("________________________Swapping Varibales___________________\n")

x = 10
y = 11

# Declaring a tuple of y,x and unpacking it on x,y
x, y = y, x


#################################################################################


# Array
print("________________________Array___________________\n")

# from array import array

numbers = array("i", [1, 2, 3, 4])

# Appends add numbers to the end of the array
numbers.append(6)
print(numbers)
# array('i', [1, 2, 3, 4, 6])

# Insert adds number to the given position in the array
numbers.insert(2, 9)
print(numbers)
# array('i', [1, 2, 9, 3, 4, 6])

numbers.remove(9)
print(numbers)
# array('i', [1, 2, 3, 4, 6])

#################################################################################


# Sets - A collection with no duplicates. They are also unordered,so we cannot access them by index
print("________________________Sets___________________\n")


numbers = [1, 1, 2, 3, 4, 5, 6, 6]
uniques = set(numbers)
print(uniques)
# {1, 2, 3, 4, 5, 6}

second = {1, 4}
second.add(5)
second.remove(4)
len(second)

numbers = [1, 1, 2, 3, 4, 5, 6, 6]
first = set(numbers)  # {1, 2, 3, 4, 5, 6}
second = {1, 3, 9}

# Union of two sets
print(first | second)
# {1, 2, 3, 4, 5, 6, 9}

# Intersection of two sets
print(first & second)
# {1, 3}

# Difference of two sets
print(first-second)
# {2, 4, 5, 6}

# Symmetric Difference - Values that are either in the first set or second set but not in both
print(first ^ second)
# {2, 4, 5, 6, 9}

if 1 in first:
    print("present")

#################################################################################


# Dictionaries - Collection of key value pair
print("________________________Dictionaries___________________\n")

point = {"x": 1, "y": 2}

point = dict(x=1, y=2)

print(point["x"])
# 1

# Modifying a key value pair
point["x"] = 10
print(point)
# {'x': 10, 'y': 2}.

# Adding a key-value pair
point["z"] = 20
print(point)
# {'x': 10, 'y': 2, 'z': 20}

# Checking if a key exist or not
if "a" in point:
    print(point["a"])

print(point.get("a", 0))
# 0

del point["x"]
print(point)
# {'y': 2, 'z': 20}

# Loop over Dict

for key in point:
    print(key, point[key])
"""
y 2
z 20
"""

# Get result in the form of tuples
for x in point.items():
    print(x)
"""
('y', 2)
('z', 20)
"""

# Unpacking tuple
for key, value in point.items():
    print(key, value)
"""
y 2
z 20
"""

#################################################################################


# Dictionaries Comprehension - Collection of key value pair
print("________________________Dictionaries Comprehension ___________________\n")

values = []
for x in range(5):
    values.append(x*2)
print(values)
# [0, 2, 4, 6, 8]

# [expression for item in items]
values = [x*2 for x in range(5)]
print(values)
# [0, 2, 4, 6, 8]

# Set comprehension
values = {x*2 for x in range(5)}
print(values)
# {0, 2, 4, 6, 8}

# Dictionary Comprehension
values = {x: x*2 for x in range(5)}
print(values)
# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

values = (x*2 for x in range(5))
print(values)
# <generator object <genexpr> at 0x0000019AAA0A8110>

#################################################################################


# Generator Expression - Iterable. It generates new value in each iteration instead of storing it in memory
print("________________________Generator Expression ___________________\n")

# Creating a list using list comprehension
values = [x*2 for x in range(10)]
for x in values:
    print(x)
"""
0
2
4
6
8
10
12
14
16
18
"""

# Creating a generator object, which is also iterable
values = (x*2 for x in range(10))
print(values)
# <generator object <genexpr> at 0x000001DD60518110>

for x in values:
    print(x)
"""
0
2
4
6
8
10
12
14
16
18
"""

# from sys import getsizeof

values = (x*2 for x in range(1000))
print("Generator ", getsizeof(values))
# Generator  208


values = [x*2 for x in range(1000)]
print("List ", getsizeof(values))
# List  8856

#################################################################################


# Unpacking Operators
print("________________________Unpacking Operators ___________________\n")

numbers = [1, 2, 3]

print(numbers)
# [1, 2, 3]

# Unpacking the list
print(*numbers)
# 1 2 3

# Normal way of generating a list
values = list(range(5))
print(values)
# [0, 1, 2, 3, 4]

# Utilizing unpacking operator
values = [*range(5)]
print(values)
# [0, 1, 2, 3, 4]

values = [*range(5), *"Hello"]
print(values)
# [0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']

first = [1, 2, 3]
second = [5, 6]
values = [*first, *second]
print(values)
# [1, 2, 3, 5, 6]

first = {"x": 1}
second = dict(x=10, y=2)

combined = {**first, **second, "z": 1}
print(combined)
# {'x': 10, 'y': 2, 'z': 1}

#################################################################################
