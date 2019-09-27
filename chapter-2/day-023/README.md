# Day 023 - Introduction to data analysis

The purpose of this task is to introduce you to the world of data analysis. This will be a brief overview, but has lots of different paths you can follow if this is something that gains your interest! We will be learning how to use `pandas` and `matplotlib`, the two most fundamental libraries in data analysis with python. Fun fact, matplotlib is based on `MATLAB`, which you may have heard of. It is very useful in cleaning, sorting, and plotting data beautifully. Combining pandas and matplotlib will give you great power over any analysis you need!

### Overview:

In your first file, `data.py`, you will take advantage of pandas nice components for storing data: Series and DataFrames (we will be focusing on DataFrames).

#####  DataFrames (df):
* Think of dictionaries in python, eg. `data = { 'hello': ['world']}`
* We can assign a variable to our df and rename our indeces, locate specific indeces, show top 10, and so on:
    * `data.loc['hello']` will return 0
    * `data.head(num of rows want to show)` --> data frame of n rows
    * `data.isnull()` --> return T/F if our data is empty


Now we will look at our `plot.py`, a good intro to plotting with python!

##### matplotlib.pyplot (plt):
* We can create arrays of data for both x,y and plot them:
    * `x=[1,2,3], y=[4,5,6] --> plt.plot(x,y) --> plt.show()` will generate our first graph!

* We can create subplots (within our figure):
    * `plt.subplot(scale factor height, sclae factor width, index)`

* We can create an figure that holds multiple axes:
    * `fig = plt.figure()`
    * `ax = fig.add_axes([list of subaxes])`
    * Then add data and `plt.show()`

* And much more! Please check these inspiring projects out, created with matplotlib and/or pandas!
    * https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/
    * https://python-graph-gallery.com/matplotlib/


### Your Task:

1. After you finish reading through this guide, visit the documentation to get an understanding how to use things

2. Install all dependencies:
    ```
    pip install pandas
    pip install matplotlib
    https://pip.pypa.io/en/stable/installing/
    ^ if you do not have pip installed on machine
    ```

3. Read over the comments inside the starter files and follow along! Feel free to explore outside the required tasks :)

We will be using https://www.sports-reference.com/ for sports stats. They allow web scraping and have very easy-to-follow web elements.

Good luck and happy coding!