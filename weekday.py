# Write a program that outputs whether or not today is a weekday. 

from datetime import datetime # https://www.delftstack.com/howto/python/python-datetime-day-of-week/#:~:text=of%20the%20day.-,Use%20the%20weekday()%20Method%20to%20Get%20the%20Name%20of,0%20and%20Sunday%20is%206.
today = datetime.today().weekday() # Returns 0-6 i.e. Monday-Sunday where 1 is Monday, 2 is Tuesday etc. 

# I made a tuple with the days of the week so i could print what day it is
daysOfWeek = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") 
print("Today is", daysOfWeek[today])

# If today is 0-4 then its a weekday, else its a weekend 
if (today == 0) or (today == 1) or (today == 2) or (today == 3) or (today == 4):
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
