# This program calculates the BMI of a person 
# Author: Shane O'Gorman 

# Input weight/height, convert to ints and store as variables
w_kg = int(input("Enter weight(kg): "))
h_cm = int(input("Enter height(cm): "))

# Calculate bmi using formula and store in variable
bmi = round((w_kg)/((h_cm/100)**2),2)

# Asigns result to the correct bmi indicator using if/else and comparison operators
if bmi < 18.5:
    result = "underweight"
elif bmi >= 18.5 and bmi <= 24.9:
    result = "normal"
elif bmi >= 25 and bmi <= 29.9:
    result = "overweight"
elif bmi >= 30 and bmi <= 34.9:
    result = "obese"
else:
    result = "extremly obese"

# Prints the BMI
print("The BMI is (kg/m^2) {}\nThis indicates the person is {}".format(bmi, result))

#References: 
#BMI formula: https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_1.html#:~:text=With%20the%20metric%20system%2C%20the,by%2010%2C000%2C%20can%20be%20used.
#Round function: https://www.w3schools.com/python/ref_func_round.asp
#BMI indicator: https://www.everydayhealth.com/diet-nutrition/bmi/bmi-adults-yours-healthy-not-how-can-you-lose-weight/
#If/else: https://www.w3schools.com/python/python_conditions.asp
#Comaparison operators: https://www.w3schools.com/python/python_operators.asp
#Format: https://www.w3schools.com/python/ref_string_format.asp