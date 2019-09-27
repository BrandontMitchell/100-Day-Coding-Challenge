import matplotlib.pyplot as plt 


# x = [1,2,3,4,5,6,7,8,9,10]  # generate x axis points    
# y = [e**2 for e in x]       # generate y-axis points

# plt.plot(x,y)
# plt.show()                  # show initial graph




# x = [1,2,3,4,5,6,7,8,9,10]  # generate x axis points    
# y = [e**3 for e in x]       # generate y-axis points

# plt.plot(x,y)
# plt.title("Our first graph") # title
# plt.xlabel("X axis label")  # x label
# plt.ylabel("Y axis label")  # y label
# plt.show()                  # show initial graph



# x = [1,2,3,4,5,6,7,8,9,10]  # generate x axis points    
# y = [e**3 for e in x]       # generate y-axis points

# plt.subplot(1, 2, 1)        # subplot init with 1/2 total width, standard height, at index 1
# plt.plot(x, y, 'red')

# plt.subplot(1, 2, 2)        # subplot init with 1/2 total width, standard height, at index 2
# plt.plot(x, y, 'blue')
# plt.show()              


# Object oriented interface
# x = [1,2,3,4,5,6,7,8,9,10]  # generate x axis points    
# y = [e**2 for e in x]       # generate y-axis points

# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.2, 0.8, 0.9])
# ax.plot(x, y, 'green')
# ax.set_xlabel("X")
# ax.set_ylabel("Y")
# ax.set_title("Title")
# plt.show()

# x = [1,2,3,4,5,6,7,8,9,10]  # generate x axis points    
# y = [e**2 for e in x]       # generate y-axis points

# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])     # add first axes to figure (from bottom left: x, y, width, height)
# ax2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])    # add second axes to figure

# ax.plot(x, y, 'green')
# ax2.plot(x, [e/2 for e in y], 'blue')       # add distinct values/color 

# ax.set_xlabel("X")
# ax.set_ylabel("Y")
# ax.set_title("Title")
# ax2.set_xlabel("X on ax2")
# ax2.set_ylabel("Y on ax2")
# ax2.set_title("Title on ax2")
# plt.show()


x = [1,2,3,4,5,6,7,8,9,10]  # generate x axis points    
y = [e**2 for e in x]       # generate y-axis points

fig, ax = plt.subplots(nrows=3, ncols=3)  # 3x3 graphs on figure
ax[0,0].plot(x,y, 'red')
ax[0,1].plot(x,y, 'red')
ax[0,2].plot(x,y, 'red')

ax[1,0].plot(x,y, 'blue')
ax[1,1].plot(x,y, 'blue')
ax[1,2].plot(x,y, 'blue')

ax[2,0].plot(x,y, 'green')
ax[2,1].plot(x,y, 'green')
ax[2,2].plot(x,y, 'green')

plt.tight_layout()
plt.show()

# https://heartbeat.fritz.ai/introduction-to-matplotlib-data-visualization-in-python-d9143287ae39