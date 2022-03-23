# Write a program that outputs whether or not today is a weekday. 
# Author: Shane O'Gorman

from datetime import datetime 
today = datetime.today().weekday() # Returns 0-6 i.e. Monday-Sunday where 1 is Monday, 2 is Tuesday etc. 

# I made a tuple with the days of the week so I could print what day it is
daysOfWeek = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") 
print("Today is", daysOfWeek[today])

# If today is 0-4 then its a weekday, else its a weekend 
if (today <= 4):
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")

# References:
# Finding what day of the week it is today: https://www.delftstack.com/howto/python/python-datetime-day-of-week/#:~:text=of%20the%20day.-,Use%20the%20weekday()%20Method%20to%20Get%20the%20Name%20of,0%20and%20Sunday%20is%206.
# Datetime module: https://www.w3schools.com/python/python_datetime.asp
# Tuples: https://www.w3schools.com/python/python_tuples.asp#:~:text=%2C%20%22cherry%22