# This program calculates the BMI of a person 
# Author: Shane O'Gorman 

w_kg = int(input("Enter weight(kg):"))
h_cm = int(input("Enter height(cm):"))

bmi = round((w_kg)/((h_cm/100)**2),2)

print("The BMI is (kg/m2) {}".format(bmi))

#Reference: 
#BMI formula https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_1.html#:~:text=With%20the%20metric%20system%2C%20the,by%2010%2C000%2C%20can%20be%20used.
#round function https://www.w3schools.com/python/ref_func_round.asp