# Write a program that reads in a text file and outputs the number of e's it contains. 

# I'm assuming the file I want is in the same folder as my program
import sys

# argv[0] is the path of my program - .\es.py i.e. the first argument i pass in the command line
# argv[1] is the second argument I pass, in this case moby-dick.txt which I set to filename
filename = sys.argv[1]

with open(filename, "rt") as f:
    count = 0 
    for line in f:
        for char in line:
            if (char == "e") or (char == "E"): # I'm assuming we are counting lower and upper case e
                count += 1
    print(count)   
    
# Needed to figure out how to go through each char in the file
# https://www.kite.com/python/answers/how-to-read-a-file-character-by-character-in-python
# How to take the filename from an argument on the command line
# https://www.youtube.com/watch?v=aMcAREDvDEo&ab_channel=ChrisHawkes