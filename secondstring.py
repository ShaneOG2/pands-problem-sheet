# Read in sentence and output every second letter in reverse order 
# Author: Shane O'Gorman

inputSentence = input("Please enter a sentence: ")

# Starts at the left side of the sentence and returns every second letter
reverseStrSecondChar = inputSentence[::-2]

print(reverseStrSecondChar)


# Reverse ref : https://www.w3schools.com/python/python_howto_reverse_string.asp
# Second letter ref : https://www.youtube.com/watch?v=w5XXa7Rw-R8&ab_channel=ProgSkill
# Slicing : https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3

