# Problem Statement
# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0


# Solution
def main():
    try: 
        num : float = float(input("Type a number to see its sqaure: "))
        square_num = str(num**2)

        print(f"The Square of {num} is {square_num}")
    except ValueError:
        print("❌ Only use Numbers !")  


if __name__ == '__main__':
    main()