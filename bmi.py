# This program calculates the BMI of a person 
# Author: Shane O'Gorman 

w_kg = int(input("Enter weight(kg):"))
h_cm = int(input("Enter height(cm):"))

bmi = round((w_kg)/((h_cm/100)**2),2)

print("The BMI is (kg/m2) {}".format(bmi))

#Reference: round function https://www.w3schools.com/python/ref_func_round.asp