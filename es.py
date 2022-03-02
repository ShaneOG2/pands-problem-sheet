#

# I'm assuming the file I want is in the same folder as my program
filename = input("What file do you wish to read in and find the number of e's? ")

with open(filename, "rt") as f:
    count = 0 
    for line in f:
        for char in line:
            if (char == "e") or (char == "E"): # I'm assuming it can be lower or upper case e
                count += 1
    print(count)                    

# Needed to figure out how to go through each char in the file
# https://www.kite.com/python/answers/how-to-read-a-file-character-by-character-in-python