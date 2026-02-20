# Conditions 
# if, elif, else

# Basic Structure 
# num = int(input("Enter a number: "))
# if num < 10:
#     print("Number is lower than 10")
# elif num == 10:
#     print("Number is equal to 10")
# else:
#     print("Number is greater than 10")

# Basic Example
# marks = int(input("Enter Your Marks: "))

# if marks > 85:
#     print("Grade A")
# elif marks > 70:
#     print("Grade B")
# elif marks > 60:
#     print("Grade C")
# elif marks > 50:
#     print("Grade D")
# else:
#     print("OOPs Grade F")

# Logical Operator 
# and, or, not 
# age = int(input("Enter your age: "))
# citizen = input("Enter your citizenship: ")

# if age > 15 or citizen == "Pak":
#     print("You are eligble")
# else:
#     print("You r not eligble")

# age = 12

# status = "Adult" if age >= 18 else "Minor"
# print(status)


# "in" in condition
# name = "Imad"
# if "a" in name:
#     print("A Contains")
# else:
#     print("A is not in the name")

# num = [1,2,3,4,5,6]
# if 1 in num:
#     print("1 Present")
# else:
#     print("1 is not in num")

# "is" in condition check memory identity 
# x = None
# if x is None:
#     print("x is None")

# logged_In = False
# if not logged_In:
#     print("Plz login first")

# Chained Comparsion
# x = 2
# if x > 5 < 20:
#     print("x is between 5 and 20")
# else:
#     print("x is out of range")

# ATM Withdrawl 
# account_balance = 5000
# withdrawal_amount = int(input("Enter amout to withdraw: "))

# if withdrawal_amount > account_balance:
#     print("Insufficient Balance")
# elif 0 < withdrawal_amount <= account_balance:
#     print("Withdrawal Successfull")
#     print("Remaining Balance",account_balance - withdrawal_amount)
# elif withdrawal_amount >= 0:
#     print("Invalid Amount")


# account_balance = 5000
# withdrawal_amount = int(input("Enter amount to withdraw: "))

# if withdrawal_amount <= 0:
#     print("Invalid Amount")

# elif withdrawal_amount > account_balance:
#     print("Insufficient Balance")

# else:
#     print("Withdrawal Successful")
#     print("Remaining Balance:", account_balance - withdrawal_amount)

# Banking Eligiblity Checker 
# Agar 18 se age km ho tu not Eligble (underage)
# Agar 18 se age zyada ho aur income 20000 se kam ho tu phr be Low-Income - not Eligble
# Agar age 18 se zyda ho aur income 20000 se zyada tu Eligble for Loan

# age = int(input("Enter your age: "))
# income = int(input("Enter your monthly income: "))

# if age < 18:
#     print("Not Eligble (underage)")
# elif age >= 18 and income < 20000:
#     print("Low-Income Not-Eligble")
# else:
#     print("Eligble for Loan")
#     print("Thank you for using our service")

# Nested if else
# agar stu ke pass studId he tu eligble he 
# agar stu k pass id he aur age less than 5 he park ticket free 
# agar stu k pass id he aur age less than or equal to 18 he park ticket 200
# agr stu k pass id he aur age greater than 18 he tu ticket 300 
# else ticket 500

# studId = True
# age = int(input("Enter ur age: "))

# if studId:
#     if age < 5:
#         print("Ticket is free for kid has studentID")
#     elif age <= 18:
#         print("Ticket for student which has studentID and age is less than or equal to 18 is RS 200")
#     elif age > 18:
#         print("Ticket for student which has studentID and age is greater than 18 is RS 300")
# else: 
#     print("Ticket price is RS 500 ")