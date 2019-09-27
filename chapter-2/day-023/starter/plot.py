import matplotlib.pyplot as plt 


x = [1,2,3,4,5,6,7,8,9,10]  # generate x axis points    
y = [e**2 for e in x]       # generate y-axis points

plt.plot(x,y)
plt.show()                  # show initial graph




# Create new plot using list comprehension
# x is values 1-10, y is values of each element in x^3
# Use axis labels!



# Create new plot with same data, but this time
# with a subplot with 1/2 total width, at index 1
# and another subplot w/ 1/2 total width at index 2      



# Lets create an object oriented interface
# with the same data (hint: use fig.add_axes)



# Create another plot (object oriented interface)
# and change the plot colors and adding x/y/title labels



# big challenge: create a plot with any data you wish to use
# that creates 9 total plots on one figure using nrows and ncols
# as a parameter in your construction of the fig, ax