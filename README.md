![Heading image](img/Shane_O'Gorman's_pands-problem-sheet.png)

## Overview ##
This respository contains my work for the 8 Pand-Problems given for Programming and Scripting. I have outlined below ... 


### Problem 1 - Body Mass Index (BMI) ###
---
**Description** - Calculate the Body Mass Index (BMI) of a person given their weight (kg) and height (cm). 

**How the program works** - 
1. The program begins by asking the user to input the weight (kg) and then height (cm). 
2. Both inputs are stored as int variables, ***w_kg*** and ***h_cm*** respectively. 
3. The formala for BMI<sup>1</sup> is: **weight (kg) / (height (m))<sup>2</sup>**. This was calculated and stored as ***bmi***. 
4. Given the inputed height was in cm, ***h_cm*** was divided by 100 in the calculation of ***bmi*** to convert to m.
5. The round function<sup>2</sup> was used to round ***bmi*** to 2 decimal places. 
6. Next, I decided to add a bit more to the program and give the user an indication<sup>3</sup> whether the BMI they got was underweight, normal, overweight, obese or extremly obese.
7. This was acheived using if/else statements<sup>4</sup> and Comparison Operators<sup>5</sup>.
8. Finally, The BMI was printed<sup>6</sup> out along with the result indicator (i.e. underweight, normal, etc.)

**References** - 
1. <a href="https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_1.html#:~:text=With%20the%20metric%20system%2C%20the,by%2010%2C000%2C%20can%20be%20used" target="_blank">BMI Formula</a>
2. <a href="https://www.w3schools.com/python/ref_func_round.asp" target="_blank">Round Function</a>
3. <a href="https://www.everydayhealth.com/diet-nutrition/bmi/bmi-adults-yours-healthy-not-how-can-you-lose-weight/" target="_blank">BMI Indicator</a>
4. <a href="https://www.w3schools.com/python/python_conditions.asp" target="_blank">If/else statements</a>
5. <a href="https://www.w3schools.com/python/python_operators.asp" target="_blank">Comparison operators</a>
6. <a href="https://www.w3schools.com/python/ref_string_format.asp" target="_blank">Format</a>

### Problem 2 - Second String ###
---
**Description** - Reads in a sentence from the user and outputs every second letter of the inputted string in reverse order. 

**How the program works** - 
1. The program begins by asking the user to input a sentence.
2. A new variable is created where the ouput string will be stored ***reverseStrSecondChar***. 
3. Firstly we need to reverse the ***inputSentence***. This is done using ***inputSentence[::-1]*** where -1 starts at the last element of the string and moves backwards through the string, outputing the reverse strings<sup>1</sup>.
4. As we want to get every second element, -1 is changes to -2<sup>2,3</sup>. 
5. Finally, every second letter of the inputted string in reverse order is printed out as a string. 

**References** - 
1. <a href="https://www.w3schools.com/python/python_howto_reverse_string.asp" target="_blank">Reverse String</a>
2. <a href="https://www.youtube.com/watch?v=w5XXa7Rw-R8&ab_channel=ProgSkill" target="_blank">Selecting every nth character from a string</a>
3. <a href="https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3" target="_blank">Slicing strings</a>

### Problem 3 - Collatz Conjecture ###
---
**Description** - ***"The Collatz conjecture in mathematics asks whether repeating two simple arithmetic operations will eventually transform every positive integer into one."***<sup>1</sup>

This program asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and: 
* If it is even, divide it by two, 
* But if it is odd, multiply it by three and add one.<sup>2</sup>

**How the program works** - 
1. The program begins by asking the user to input a positve integer.
2. Then a list is created and the inputed postive integer is added to the list.
3. Given the Collatz conjecture, we assume by repeating the two arithmetic operations (for even and odd numbers), we will eventually transform every positive integer to one. Therefore, we use a while loop where num is greater than 1.<sup>3</sup>
4. Using an if/else statement we check whether num is even or odd. 
5. If even, num is set to num divided by 2. If even, num is set to 3 multiplied by num plus 1. 
6. The result of the calculation is appended to the list.<sup>4</sup>
7. Due to the while loop steps 4-6 are repeated until num is equal to 1. 
8. Finally, the list of the Collatz sequenece of the inputed number is printed to the screen.<sup>5</sup>

**References** - 
1. <a href="# Wikipedia - Collatz conjecture: https://en.wikipedia.org/wiki/Collatz_conjecture" target="_blank">Wikipedia - Collatz conjecture</a>
2. <a href="https://www.youtube.com/watch?v=094y1Z2wpJg" target="_blank">Understanding problem</a>
3. <a href="https://www.w3schools.com/python/python_while_loops.asp" target="_blank">While loops</a>
4. <a href="# Appending elements to list: https://www.w3schools.com/python/ref_list_append.asp" target="_blank">Appending elements to list</a>
5. <a href="https://stackoverflow.com/questions/3249524/print-in-one-line-dynamically" target="_blank">Print elements of list on one line</a>

### README References ###
Ideas for README: https://www.youtube.com/watch?v=ECuqb5Tv9qI&t=158s&ab_channel=codeSTACKr
https://www.youtube.com/watch?v=a8CwpGARAsQ&ab_channel=Mr.RandomGenerator
Banner Maker: https://banner.godori.dev
Markdown cheat sheet: https://www.markdownguide.org/basic-syntax/#blockquotes-1

