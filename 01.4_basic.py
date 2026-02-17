# Input 
# Input is a function that allows us to get user input from the console. It takes a string as an argument, which is displayed as a prompt to the user. The function then waits for the user to enter some text and press the Enter key. Once the user does this, the function returns the entered text as a string.

name = input("Enter your name: ")
print(name)
x = input("Enter first number: ")
y = input("Enter second number: ")
print(int(x) + int(y))