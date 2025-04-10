# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# Solution

# There are 12 inches for 1 foot
INCHES_IN_FOOT : int = 12

def main():
    """
    Conversion of Feet Into Inches 
    """
    try:
        print(50*"-")
        print("Conversion of Feet Into Inches!")
        feet: float = float(input("Enter the number of feet: "))
        convert_in_inches: float = feet * INCHES_IN_FOOT
        print(f"The Conversion of {feet} feet in inches = {convert_in_inches}inches")
        print(50*"-")
    except  ValueError:
        print("❌ Feet always in Number !") 


if __name__ == '__main__':
    main()
