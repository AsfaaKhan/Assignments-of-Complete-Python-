# Problem Statement
# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

# Here's a sample run of the program (user input is in blue):

# How old are you? 20 You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.

# Solution:
PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48


def main():
    user_age = int(input("How old are you? "))

    # Check the condition for voting 
    # Condition 1 -> For Peturksbouipo 
    if user_age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo(Scotland, Ethiopia, and Austria) where the voting age is : {str(PETURKSBOUIPO_AGE)}.")
    else :
        print(f"You cannot vote in Peturksbouipo(Scotland, Ethiopia, and Austria) where the voting age is : {str(PETURKSBOUIPO_AGE)}.")

    # Condition 2 -> Stanlau 
    if  user_age >= STANLAU_AGE:
        print(f"You can vote in Stanlau(United Arab Emirates) where the voting age is : {str(STANLAU_AGE)}.")
    else:
        print(f"You cannot vote in Stanlau(United Arab Emirates) where the voting age is : {str(STANLAU_AGE)}.")

    # Condition 3 -> Mayengua 
    if user_age >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua(In real life, this isn't the voting age anywhere) where the voting age is : {str(MAYENGUA_AGE)}.")
    else:
        print(f"You cannot vote in Mayengua(In real life, this isn't the voting age anywhere) where the voting age is : {str(MAYENGUA_AGE)}.")
    

if __name__ == '__main__':
    main()
