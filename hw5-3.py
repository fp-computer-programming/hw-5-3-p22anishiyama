# Author: ATN 10/26/21

import calendar

# Question 1
calendar.TextCalendar().pryear(2020)

# Question 2
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prcal(2020)

# Question 3
calendar.prmonth(2020, 11)

# Question 4 but a lot of errors
# calendar.LocaleTextCalendar(6, "SPANISH").pryear(2020)

# Question 5
print(calendar.isleap(2020))
# Returns a boolean because 2020 is a leap year
