# Problem Statement
# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.

# Solution

def sum():
    try:
        num1 : str = int(input("Enter The First Number:"))
        num2 : str = int(input("Enter The Second Number:"))
        total_sum = num1 + num2
        print("The Sum of The numbers are " , total_sum, ".")
    except ValueError:
        print("❌ Only use Numbers !!")




# I Add Additional Feathers in this program 

def main():
    try:
        num1 : str = int(input("1️  Enter The First Number:"))
        num2 : str = int(input("2️  Enter The Second Number:"))
        operation = input("📊 Select The Operater: ( + ,- , * , / ) ")
        if(operation == "+"):
            add = num1 + num2
            print("✅ The Addition of Two Numbers are ", add, ".")
        elif(operation == "-"):
            sub = num1 - num2
            print("✅ The Subtration of Two Numbers are ", sub, ".")
        elif(operation == "*"):
            multiply = num1 * num2
            print("✅ The Multiply of Two Numbers are ", multiply, ".")
        elif(operation == "/"):
            divide = num1 / num2
            print("✅ The Divion of Two Numbers are ", divide, ".") 
        else: 
            print("❌ Select options from this ( + , - , * , / ) ")
    except ValueError:
        print("❌ Only use Numbers !!")
        exit

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    sum()
    print(50*"-")
    main() 
  