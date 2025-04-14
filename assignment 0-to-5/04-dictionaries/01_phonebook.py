# Problem Statement
# In this program we show an example of using dictionaries to keep track of information in a phonebook.

# Solution
def  read_phone_numbers():
    """
    Ask the users for names/numbers to store in a phonebook.
    """
    phonebook = {}

    while True:
        name = input("Enter a name: ")
        if name == "":
            break
        number = input("Enter a number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    """
    Print out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(str(name) + " -> "+ str(phonebook[name]))


def lookup_numbers(phonebook):
    """
    Allow user the lookup phone numbers in the phonebook by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])  

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

if __name__ == "__main__":
    main()      