# Problem Statement
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.


# Soluton

def get_first_elelmet(list):
    """Print the first element of the given non-empty list."""
    print(f"The first element in list is : {list[-1]}")

# Taking input from the user:
n = int(input("Enter the numbers of element in the list: "))
list = []

for i in range(n):
    element= input(f"Enter Element {i+1}: ")
    list.append(element)
   

print(list)
get_first_elelmet(list)

