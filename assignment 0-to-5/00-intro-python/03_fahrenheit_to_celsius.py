# Problem Statement
# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

# The equation you should use for converting from Fahrenheit to Celsius is the following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# (Note. The .0 after the 5 and 9 matters in the line above!!!)

# Here's a sample run of the program (user input is in bold italics):

# Enter temperature in Fahrenheit: 76

# Temperature: 76.0F = 24.444444444444443C

#------------------------------------------------------------------------#

# Solution
def main():
    try:
        print(50*"-")
        selection = input("Select option you want to convert : \n1. Fahreheit to Celsius \n2. Celsius to Fahreheit \nOption Select: ")
        if selection == "1":
                fahrenheit_temp  = float(input("Enter Temperatur: "))
                calsius_temp = (fahrenheit_temp - 32)*5/9
                print(f"Fahreheit Temperature : {fahrenheit_temp}F = Celsius Temperature = {calsius_temp:.3f}°C") # .3f -> in float integer 3 decimal place is shown
        elif selection == "2":
                calsius_temp  = float(input("Enter Temperatur: "))
                fahrenheit_temp = (calsius_temp  *5/9)+32
                print(f"Celsius Temperature:  {calsius_temp}°C = Fahreheit Temperature : {fahrenheit_temp:.3f}F ") # .3f -> in float integer 3 decimal place is shown
        else: 
            print("❌ Select Valid Option ")

        print(50*"-")

    except ValueError: 
        print("❌ Only add numbers to  convert the temperature from farenheit to celcius! ")

if __name__ == "__main__":
    main()
