![Heading image](img/Shane_O'Gorman's_pands-problem-sheet.png)

## Overview ##
This respository contains my work for the Pand-Problems given for Programming and Scripting course. I have outlined below each problem with a brief description, how the program works and the references I used to when writing the program. 


### Problem 1 - Body Mass Index (BMI) ###
---
**Description** - Calculate the Body Mass Index (BMI) of a person given their weight (kg) and height (cm). 

**How the program works** - 
1. The program begins by asking the user to input the weight (kg) and then height (cm). 
2. Both inputs are stored as int variables, ***w_kg*** and ***h_cm*** respectively. 
3. The formala for BMI<sup>1</sup> is: **weight (kg) / (height (m))<sup>2</sup>**. This was calculated and stored as ***bmi***. 
4. Given the inputed height was in cm, ***h_cm*** was divided by 100 in the calculation of ***bmi*** to convert to meters.
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
1. The program begins by asking the user to input a positve integer. If the user inputs an integer less than 0 an error is thrown and the programs stops.<sup>3</sup>
2. Then a list is created and the inputed postive integer is added to the list.
3. Given the Collatz conjecture, we assume by repeating the two arithmetic operations (for even and odd numbers), we will eventually transform every positive integer to one. Therefore, we use a while loop where ***num*** is greater than 1.<sup>4</sup>
4. Using an if/else statement we check whether ***num*** is even or odd. 
5. If even, ***num*** is set to ***num*** divided by 2. If even, ***num*** is set to 3 multiplied by ***num*** plus 1. 
6. The result of the calculation is appended to the list.<sup>5</sup>
7. Due to the while loop steps 4-6 are repeated until ***num*** is equal to 1. 
8. Finally, the list of the Collatz sequenece of the inputed number is printed to the screen.<sup>6</sup>

**References** - 
1. <a href="https://en.wikipedia.org/wiki/Collatz_conjecture" target="_blank">Wikipedia - Collatz conjecture</a>
2. <a href="https://www.youtube.com/watch?v=094y1Z2wpJg" target="_blank">Understanding problem</a>
3. <a href="https://web.microsoftstream.com/video/625784d5-114f-4f8b-a929-8d46a63297ad" target="_blank">Exceptions and errors</a>
4. <a href="https://www.w3schools.com/python/python_while_loops.asp" target="_blank">While loops</a>
5. <a href="https://www.w3schools.com/python/ref_list_append.asp" target="_blank">Appending elements to list</a>
6. <a href="https://stackoverflow.com/questions/3249524/print-in-one-line-dynamically" target="_blank">Print elements of list on one line</a>

### Problem 4 - Weekday ###
---
**Description** - The program outputs what day it is and whether it is a weekday or not.  

**How the program works** - 
1. The program begins by setting the variable ***today*** to the day of the week it is. ***datetime.today().weekday()*** returns 0-6 i.e. Monday-Sunday where 0 is Monday, 1 is Tuesday etc.<sup>1/2</sup>
2. I then created a tuple ***daysOfWeek*** with the days of week beginning with Monday and ending in Sunday.<sup>3</sup> 
3. Using the tuple ***daysOfWeek*** and varible ***today***, the program could then print what day of the week it is.
4. An if/else statement was used to determine if ***today*** was a weekday or a weekend.  

**References** - 
1. <a href="https://www.delftstack.com/howto/python/python-datetime-day-of-week/#:~:text=of%20the%20day.-,Use%20the%20weekday()%20Method%20to%20Get%20the%20Name%20of,0%20and%20Sunday%20is%206." target="_blank">Finding what day of the week it is today</a>
2. <a href="https://www.w3schools.com/python/python_datetime.asp" target="_blank">Datetime module</a>
3. <a href="https://www.w3schools.com/python/python_tuples.asp#:~:text=%2C%20%22cherry%22" target="_blank">Tuples</a>

### Problem 5 - Square Root ###
---
**Description** - The program takes a positive floating-point number as input and outputs an approximation of its square root. 

This was done using Newton's Method.<sup>1</sup>

General Formula: <br/>
**x<sub>n+1</sub> = x<sub>n</sub> - (f(x<sub>n</sub>)/f'(x<sub>n</sub>))**

Equation for Square Roots: <br/>
**f(x) = x<sup>2</sup> - num** <br >
**f'(x) = 2x**

Subbing into the gerneral formula we get: <br/>
**x<sub>n+1</sub> = x<sub>n</sub> - ((x<sub>n</sub><sup>2</sup> - num)/(2x<sub>n</sub>))**

**How the program works<sup>2</sup>** - 
1. The program begins with the function ***sqrt()*** with parameters ***num*** and ***error*** set to 0.00001.
2. The first ***guess*** is set to the number we want the square root of. 
3. ***Diff*** is set to a large number. 
4. A while loop is repeated while ***diff*** is greater than ***error***. 
5. ***newGuess*** is calculated by applying Newton's Method. 
6. ***Diff*** is reset to the absolute differece of our first guess and new guess. 
7. ***guess*** is set to ***newGuess*** and the loop is repeated until we achieve a square root that is less than the ***error*** we specified. 

**References** - 
1. <a href="https://en.wikipedia.org/wiki/Newton%27s_method" target="_blank">Newton's Method</a>
2. <a href="https://www.youtube.com/watch?v=tUFzOLDuvaE&ab_channel=0612TVw%2FNERDfirst" target="_blank">How to calculate square roots using Newton's Method</a>

### Problem 6 - Number of e's ###
---
**Description** - The program reads in a text file and outputs the number of e's it contains. The program takes the filename from an argument on the command line. 

**How the program works** - 
1. Using the sys module we can use argv to take in the filename we want from the command line<sup>1</sup>. 
2. ***arg[0]*** is the path of my program - .\es.py i.e. the first argument I pass in the command line. 
3. ***arg[1]*** is the second argument I pass, in this case moby-dick.txt which I set to filename. 
4. We then need to read in the file<sup>2</sup>. 
5. Using a nested for loop we can loop through each character<sup>3</sup> in the file and increment ***count*** each time "e" or "E" occurs.
6. Finally, the number of "e" or "E"s is printed. 

**References** - 
1. <a href="https://www.youtube.com/watch?v=aMcAREDvDEo&ab_channel=ChrisHawkes" target="_blank">How to take the filename from an argument on the command line</a>
2. <a href="https://www.w3schools.com/python/python_file_handling.asp" target="_blank">Opening file</a>
3. <a href="https://www.kite.com/python/answers/how-to-read-a-file-character-by-character-in-python" target="_blank">Checks each character in file</a>

## Problem 7 - Plot task ###
---
**Description** - The program displays a plot of three functions with the range [0,4]: 

f(x) = x
g(x)= x<sup>2</sup>
h(x)= x<sup>3</sup>

**How the program works** - 
1. Firstly, the program gets the x-points to plot - using np.arrange we can get the points between 0-4 incremented by 0.1 for accuracy<sup>1</sup>. This is inputed into a numpy array. 
2. We can then calculate or y-points based off our x-points for each of the three functions f(x), g(x) and h(x). 
3. We can then plot the fuctions using ***plt.plot()*** giving each function a different colour and labeling them.
4. ***plt.legend()*** shows the fuction labels and colour to distinguish between them<sup>4</sup>.
5. I added "Functions" as the title of the plot along with labeling the x and y axis. 
6. plt.xticks and plt.yticks were used to get the correct x and y axis label increments i.e on the x axis I wanted 0, 1, 2, 3, 4 to be shown and on the y axis 0 - 70 with increments of 10.<sup>3</sup>
7. ***plt.grid()*** puts grid lines on the plot. 
8. Finally, 4. ***plt.show()*** shows the plot we created. 

**References** - 
1. <a href="https://pynative.com/python-range-for-float-numbers/" target="_blank">Used to get more x-points</a>
2. <a href="https://www.w3schools.com/python/matplotlib_labels.asp" target="_blank">Design of plot</a>
3. <a href="https://stackabuse.com/how-to-set-axis-range-xlim-ylim-in-matplotlib/" target="_blank">Design of plot (Axis labels)</a>
4. <a href="https://stackoverflow.com/questions/21226868/superscript-in-python-plots" target="_blank">Power of formating</a>

### README References ###
1. <a href="https://www.youtube.com/watch?v=ECuqb5Tv9qI&t=158s&ab_channel=codeSTACKr" target="_blank">Ideas for README 1</a>
2. <a href="https://www.youtube.com/watch?v=a8CwpGARAsQ&ab_channel=Mr.RandomGenerator" target="_blank">Ideas for README 2</a>
3. <a href="https://banner.godori.dev/" target="_blank">Banner Maker</a>
3. <a href="https://www.markdownguide.org/basic-syntax/#blockquotes-1" target="_blank">Markdown Cheat Sheet</a>