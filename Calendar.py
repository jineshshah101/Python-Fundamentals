import calendar

#figuring things out with calendar

# printing out the week headers
# using the number 3 so we can get 3 characters for the week header
week_header = calendar.weekheader(3)
print(week_header)
print()

# print out the index value that represents a weekday
# in this case we are getting the index of the first weekday
# [0,1,2,3,4,5,6] correlates to Mon, Tue, Wed, Thu, Fri, Sat, Sun
weekday_index = calendar.firstweekday()
print(weekday_index)
print()

# print out the march month of 2019
# w stands for the number of characters shown for the week header
march_month = calendar.month(2019, 3, w=3)
print(march_month)
print()

# print out the days of a month in a matrix format
# in this case this is for march 2019
matrix_month_march = calendar.monthcalendar(2019, 3)
print(matrix_month_march)
print()

# print out the calendar for the entire year of 2020
entire_year = calendar.calendar(2020, w=3)
print(entire_year)
print()

# prints out the day of the week based on specific specifications in index format
day_of_the_week = calendar.weekday(2020, 1, 15)
print(day_of_the_week)
print()

# will tell you if a certain year is a leap year or not
leap_year = calendar.isleap(2020)
print(leap_year)
print()

# print out the number of leapdays within the specified years
# note: year 2 is not included in this search
leap_days_amount = calendar.leapdays(2000, 2021)
print(leap_days_amount)