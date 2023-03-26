import matplotlib.pyplot as plt
import numpy as np

def square(x):
    return x**2

x_values = np.arange(100)
y_values = [square(x) for x in x_values]

interp_x = np.arange(0, 100, 24.5) # range of x values to interpolate at
interp_y = []

# linear interpolation
for x in interp_x:
    i = 0
    while i < len(x_values) - 1 and x > x_values[i+1]: # Find the two closest x values
        i += 1
        
    slope = (y_values[i+1] - y_values[i]) / (x_values[i+1] - x_values[i])
    y = y_values[i] + slope * (x - x_values[i])
    
    interp_y.append(y)


interp_y_numpy = np.interp(interp_x, x_values, y_values)

#git statusplt.plot(interp_x, interp_y_numpy, label='Linear interpolation - numpy')
plt.plot(interp_x, interp_y, label='Linear interpolation')
plt.plot(x_values, y_values, '.', label='Square function')
plt.legend()
plt.show()
