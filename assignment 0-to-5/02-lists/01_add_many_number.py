# Problem Statement
# Write a function that takes a list of numbers and returns the sum of those numbers.

# Solution



def sum_of_numbers(numbers) -> int:
    add_numbers : int = 0
    for number in numbers :
        add_numbers += number
    return add_numbers

answer = sum_of_numbers([1,2,3,5,6])    
print(answer)

