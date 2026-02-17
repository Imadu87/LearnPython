# Data Types 

# Strings
name = "Ali Khan"
print(type(name))
print(len(name))
print(name[0:3])

# Numbers 
a = 4
b = 3.2
print(type(a)) # integer
print(type(b)) # float

# Boolean
is_active = False 
is_admin = True
print(type(is_active))

# NoneType
# Special type of python like JS has null, undefined
c = None
print(type(c))

# List 
# Like array in JS
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits.append("mango")
fruits[0] = "apricot"
print(fruits)
# Mutable: It can be changed 
# Ordered: Maintain indexing


# Tuple # Like list but immutable
colors = ("red", "yellow", "white")
print(colors[0])
# colors[0] = "brown" # Tuple is imutable

# Set 
# unorderd, unique elements
numbers = {1, 2, 3, 4, 5, 6, 6}
print(numbers) # Duplicate remove

# Dictionary 
person = {
    "name": "Ali",
    "age": 25,
    "city": "Karachi"
}
print(person["age"])
person["country"] = "Pakistan" # Add new key
print(person)

# Advanced Data Types 
# Complex number 
z = 3 + 4j
print(type(z))
print(z.real)
print(z.imag)

# Range (generate numbers in sequence)
r = range(0, 20, 4)
print(list(r))

# Bytes
b = b"hello"
print(type(b))  # <class 'bytes'>