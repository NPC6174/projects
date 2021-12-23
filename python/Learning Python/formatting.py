#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
# Times and dates can be formatted using a set of predefined string control codes
    now = datetime.now()

#### DATE FORMATTING ####

# %y/%Y - Year, %a/%A - Weekday, %b/%B - Month, %d - Day of Month
    print(now.strftime("The current abbreviated year is: %y"))
    print(now.strftime("The current full year is: %Y"))
    print(now.strftime("The current abbreviated weekday is: %a"))
    print(now.strftime("The current full weekday is: %A"))
    print(now.strftime("The current abbreviated month is: %b"))
    print(now.strftime("The current full month is: %B"))
    print(now.strftime("The current day of the current month is: %d"))

# %c - Locale's date and time, %x - Locale's date, %X - Locale's time
    print(now.strftime("The current locale date and time is: %c"))
    print(now.strftime("The current locale date is: %x"))
    print(now.strftime("The current locale time is: %X"))

#### TIME FORMATTING ####

# %I/%H - 12/24 Hour, %M - Minute, %S - Second, %p - Locale's AM/PM
    print(now.strftime("The 12 hour component of the current time is: %I"))
    print(now.strftime("The 24 hour component of the current time is: %H"))
    print(now.strftime("The minute component of the current time is: %M"))
    print(now.strftime("The second component of the current time is: %S"))
    print(now.strftime("The AM/PM component of the current locale time is: %p"))
    print(now.strftime("The 12 hour long version of the current locale time is: %I:%M:%S %p"))
    print(now.strftime("The 124 hour long version of the current locale time is: %H:%M:%S"))


if __name__ == "__main__":
    main()