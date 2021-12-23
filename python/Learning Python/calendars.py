#
# Example file for working with calendars
#

# TODO: Import the calendar module
import calendar

# TODO: Create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2022, 1, 0, 0)
print(str)

# TODO: Create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2022, 1)
print(str)

# TODO: Loop over the days of a month
# Zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2022, 8):
    print(i)

# TODO: The calendar module provides useful utilities for the given locale, 
# Such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# TODO: Calculate days based on a rule: For example, consider
# A team meeting on the first Friday of every month
# To figure out what days that would be for each month,
# We can use this script:
print("Team meetings will be on:")
for m in range(1, 13):
    cal = calendar.monthcalendar(2022, m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print(calendar.month_name[m], meetday)

