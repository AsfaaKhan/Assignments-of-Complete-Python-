# Problem Statement
# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

# Solution

MAX_LENGTH = 3

def shorten_list(list):
    while len(list) > MAX_LENGTH:
        last_element = list.pop()
        print(last_element)

def get_list():
    """
    Prompt the user to enter one element of the list  at a time and return the result in:
    """ 
    list = []
    element = input("Please enter an element of the list or press enter to stop: ")       
    while element != "":
        list.append(element)
        element = input("Please enter an element of the list or press enter to stop: ") 
            
    return list  

def main():
    list = get_list()
    print(list)
    shorten_list(list)


if __name__ == '__main__':
    main()   
