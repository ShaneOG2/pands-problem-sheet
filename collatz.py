# Asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one.
# Author: Shane O'Gorman

num = int(input("Please enter a positive integer: ")) # This allows all integers. 
# Andrew mentioned error statements so wait til he discusses and then ammend
arr = [num] # Creates list and adds first inputed number to it 

while num > 1: # Keeps running while calculations are greater than 1 and until we get to 1 
    if num % 2 == 0: # Checks that the number is even and if so divides by one
        num = num/2
    else: # Checks if the number is odd and if so multiplies num by 3 and adds 1
        num = 3*num + 1
    arr.append(int(num)) # Adds the newly calculated to the list/Converts float to int

print("The Collatz sequence of {} is: ".format(arr[0]))

for num in arr:
    print(num, end = " ")

# References:
# Wikipedia - Collatz conjecture: https://en.wikipedia.org/wiki/Collatz_conjecture
# Understanding problem: https://www.youtube.com/watch?v=094y1Z2wpJg&ab_channel=Veritasium
# Appending elements to list: https://www.w3schools.com/python/ref_list_append.asp
# Print elements of list on one line: https://stackoverflow.com/questions/3249524/print-in-one-line-dynamically