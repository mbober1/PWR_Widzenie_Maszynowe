import matplotlib.pyplot as plt
import numpy as np

def square(x):
    return x**2

x_values = np.arange(26)
y_values = [square(x) for x in x_values]

interp_x = np.arange(0, 26, 5) # range of x values to interpolate at
interp_y_linear = []

# LINEAR
for x in interp_x:
    i = 0
    while i < len(x_values) - 1 and x > x_values[i+1]: # Find the two closest x values
        i += 1
        
    slope = (y_values[i+1] - y_values[i]) / (x_values[i+1] - x_values[i])
    y = y_values[i] + slope * (x - x_values[i])
    
    interp_y_linear.append(y)

interp_y_np_linear = np.interp(interp_x, x_values, y_values)


# NEAREST NEIGHBOUR
interp_y_nn = []
for x in interp_x:
    # Find the index of the closest x value in x_values
    index = min(range(len(x_values)), key=lambda i: abs(x_values[i]-x))
    
    # Add the corresponding y value to the interp_y list
    interp_y_nn.append(y_values[index])



# LINEAR INTERPOLATION
plt.plot(interp_x, interp_y_np_linear, label='Linear interpolation - numpy')
plt.plot(interp_x, interp_y_linear, label='Linear interpolation')
plt.plot(x_values, y_values, '.', label='Square function')
plt.legend()
plt.show()


# NN using numpy
#interp_x_np = np.linspace(0, 26, num=100)
#interp_y_np_nn = y_values[np.searchsorted(x_values, interp_x_np, side='left')]

# NN INTERPOLATION
#plt.plot(interp_x, interp_y_np_nn, label='Nearest neighbor interpolation - numpy')
plt.plot(interp_x, interp_y_nn, label='Nearest neighbor interpolation')
plt.plot(x_values, y_values, '.', label='Square function')
plt.legend()
plt.show()
