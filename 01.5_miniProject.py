# Calculator 

x = input("Enter first Number: ")
y = input("Enter the operator: ")
z = input("Enter second Number: ")

if y == "+":
    print(int(x) + int(z))
elif y == "-":
    print(int(x) - int(z))
elif y == "*":
    print(int(x) * int(z))
elif y == "/":
    print(int(x) / int(z))