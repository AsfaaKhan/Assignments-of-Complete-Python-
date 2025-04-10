# Problem Statement
# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

# Solution

def get_first_elelmet(list):
    """Print the first element of the given non-empty list."""
    print(f"The first element in list is : {list[0]}")

# Taking input from the user:
n = int(input("Enter the numbers of element in the list: "))
list = []

for i in range(n):
    element= input(f"Enter Element {i+1}: ")
    list.append(element)
   

print(list)
get_first_elelmet(list)




