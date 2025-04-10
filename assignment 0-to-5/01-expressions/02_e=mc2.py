# Problem Statement
# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

# Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

# Here's a sample run of the program (user input is in bold italics):

# Enter kilos of mass: 100

# e = m * C^2...

# m = 100.0 kg

# C = 299792458 m/s

# 8.987551787368176e+18 joules of energy!

# Solution
# Speed of light 
C : int  =   299792458
def main():
    try:
        mass_in_kg : float = float(input("Enter kilos of mass: "))
        
        # Calculate Energy Formula of energy :
        energy_in_joules : float = mass_in_kg * (C**2)

        print("The Formula of Energy { e = m * C ^ 2 } ")
        print("m = " , str(mass_in_kg), "kg")
        print("C = "+ str(C) + "m/s")
        print(f"Energy in joules {energy_in_joules} joules energy")
    except ValueError:
        print("❌ Mass is always in Number!")    

if __name__ == '__main__':
    main()    