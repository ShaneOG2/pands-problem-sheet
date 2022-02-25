# Write a program that takes a positive floating-point number as input and outputs an 
# approximation of its square root. 

# Author: Shane O'Gorman

# References
# https://en.wikipedia.org/wiki/Newton%27s_method
# https://www.youtube.com/watch?v=tUFzOLDuvaE&ab_channel=0612TVw%2FNERDfirst
# General Formula = X(n+1) = X(n) - f(X(n))/f'(X(n))
# Equaltions for square roots - f(X) = x^2 - num (num = sqrt of the number we want to get)
# f'(x) = 2x
# Subbing into general formula we get - 
# X(n+1) = X(n) - (X(n)^2-num)/2X(n)
 
def sqrt(num, error = 0.00001):
	guess = num	# First guess is just num itself
	diff = 999999999 # diff is used to check terminating condition. Set to large number
	while diff > error:
		newGuess = guess - ((guess**2 - num) / (2*guess)) # Apply Newton's Method
		
		# Calculate the absolute difference between the two guesses
		diff = newGuess - guess
		if diff < 0:
			diff *= -1
			
		# Update existing guess
		guess = newGuess
		
	return guess


