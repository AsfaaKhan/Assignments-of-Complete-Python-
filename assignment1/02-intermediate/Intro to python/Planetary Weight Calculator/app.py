# Problem: Planetary Weight Calculator
# Milestone #1: Mars Weight
# A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity. Ingenuity made its third flight, during which it flew faster and further than it had on any of its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!

# Ingenuity on the surface of Mars (source: NASA)

# When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars, an Earthling's weight on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars.

# The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. You pass in the value to be rounded and the number of decimal places to use. In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14.

# Solution

def access_element(lst, index):
    try: 
        return lst[index]
    except IndexError:
        return "Index is out of range."
    
def modify_element(lst,index,new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index is out of range"
    
def slice_list(lst,start,end):
    try:
        return lst[start:end]
    except IndexError :
        return "Invalid Indices."

def index_game():
    lst = [1,2,3,4,5] 
    print("Current list ", lst)
    print("\nChoose an operation:\n1. Access,\n2. Modify,\n3. Slice\n")
    operation = input("Enter Operation: ")
    if operation == "1":
        index = int(input("Enter index to access: "))
        print(access_element(lst, index))

    elif operation == "2":
        index = int(input("Enter index to mofify: "))
        new_value = int(input("Enter new value: "))
        print(modify_element(lst,index,new_value))   
    elif operation == "3":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(lst,start,end))
    else:
        print("Invalid operation.")

index_game()
