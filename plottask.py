# Displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author: Shane O'Gorman

from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

# I wanted to get more points for x for accuracy. Range() wouldn't allow for float types. 
xpoints = np.array(np.arange(0,4.1,0.1))

# Getting y-points for each of the three functions f(x), g(x) and h(x). 
f_ypoints = xpoints
g_ypoints = xpoints**2
h_ypoints = xpoints**3

# Plots each of the three fuctions, gives them each a colour and label
plt.plot(xpoints,f_ypoints,color="r",label="f(x)=x")
plt.plot(xpoints,g_ypoints,color="g",label="g(x)=x^2")
plt.plot(xpoints,h_ypoints,color="b",label="h(x)=x^3")

plt.legend() # Displays legend table

# Titles plot and labels axis
plt.title("Functions", loc = 'center') 
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

#plt.ylim([0,80])
plt.xticks([0,1,2,3,4]) # Just shows whole numbers on x-axis
plt.yticks(range(0,71,10)) # Y-Axis did not show 70 so added it in
plt.grid() # Places grid lines on plot

plt.show()

# Reference = https://pynative.com/python-range-for-float-numbers/ - Used to get more points for x-axis
# https://www.w3schools.com/python/matplotlib_labels.asp - Design of plot  
# https://stackabuse.com/how-to-set-axis-range-xlim-ylim-in-matplotlib/ - Design of plot (Axis labels)
