# Problem Statement
# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

# Solution

DAYS_PER_YEAR : int = 365
HOURS_PER_DAY : int = 24
MIN_PER_HOUR : int = 60
SECONDS_PER_MIN : int = 60

def main():
    total_seconds_in_year : int = int(DAYS_PER_YEAR*HOURS_PER_DAY*MIN_PER_HOUR*SECONDS_PER_MIN)
    print(total_seconds_in_year)
    print(f"There are {total_seconds_in_year} seconds in year." )

if __name__ =='__main__':
    main()