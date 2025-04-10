# Problem Statement
# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2


# Solution
def main():
    try:
        # Get the numbers from the users
        print(50*"-")
        dividend : int  = int(input("Please enter the number to be divide: "))
        divisor : int = int(input("Please enter the number to divide by:"))

        quotient : int = dividend // divisor
        remainder : int = dividend % divisor
        print(f"The result of this division is {quotient} with the remainder of {remainder}")
        print(50*"-")
    except ValueError:
        print("❌ Please enter the number only! ")

if __name__=='__main__':
    main()    
 