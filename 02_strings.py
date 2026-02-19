# String

# Making strings has 3 types 
# a = "Apple in double quotes"
# b = 'Apple in single quote'
# c = '''Apple 
# In triple quotes
# '''
# print(a, b, c)
# The triple quotes are used to define strings in multiple lines

# Strings are imutable whenever we change the string so make new string 
# d = "Ali"
# d[0] = "B"
# print(d) This is incorrect b/c string is imutable you can never change it.

# Indexing
# name = "Python"
# print(name[0]) # P
# print(name[-1]) # reverse indexing last one (n)
# print(name[-2]) # reverse indexing second last one (o)

# Scliceing
# name[start:end:step]
# print(name[0:3]) # start and end 
# print(name[:3]) # end 
# print(name[::2]) # steps
# print(name[0:5:1]) # start:end:steps
# In sclicing the last one is not included
# reverse step
# print(name[::-1])

# String concatation 
# first_name = "Imad"
# last_name = "Uddin"
# full_name = first_name + " " + last_name
# print(full_name)

# String + number are not allowed 
# age = 25
# data = full_name + " " + age # Not allowed
# data = full_name + " " + str(age)
# print(data)

# String formating 
# name = "Ali"
# age = 20
# print(f"My name is {name} and I am {age} years old.")
# print(f"2 + 2 = {2 + 2}") # You can use expression
# print(f"100 + 2 = {100 + 2}")

# String Method 
# Lower and Upper 
# name = "Imad"
# print(name.upper())
# print(name.lower())

# Strip() method use to remove extra spaces 
# contact = "            1234  "
# print(contact)
# print(contact.strip())

# replace method 
# text = "Hello World"
# print(text.replace("World", "Python"))
# print(text.replace("Hello World", "Helllllllo Python!"))

# Split method
# List has been make
# fruits = "apple, banana, mango"
# print(fruits.split(",")) # Output like: ['apple', ' banana', ' mango']
# example
# students = "ali, ahmad, Imad, Khan"
# print(students.split(","))

# Join Method
# items = ["apple", "banana", "mango"]
# print(",".join(items))
# Make apple,banana,mango from the list

# Find Method 
# return index
# course = "Hello Python"
# print(course.find("Python"))

# String Checking Method 
# To check letters only 
# return true or false 
# name = "Apple123"
# # print(name.isalpha()) # check only letters 
# print(name.isdigit()) # check only digits
# print(name.isalnum()) # check both letters and number
# print(name.startswith("A")) # return True / False
# print(name.endswith("A")) # return True / False

# city = "Peshawar"
# print(city.isalpha())

# Escape Character 
# Both are correct 
# apple1 = 'He wanted, \"I have eat an apple\"'
# apple = 'He wanted, "I have eat an apple"'
# print(apple)
# print(apple1)

# print("He said, \"Hello\"")
# print("Line 1\nLine 2")
# print("tab\tSpace")

# Memory Concept (Advanced)
# Python uses sometimes memory concepts
# a = "hello"
# b = "hello"
# print(id(a))
# print(id(b))
# Both id are same 