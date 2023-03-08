#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

# weż jakąć funkcję np x^2 

# interpolacja NN i interpolacja liniowa
# interpolacja scipy
# porównać wyniki MSE (mean squared error) oraz czas wykonania

def interpolation_scipy(x, y, x_target):
  y_interp = interp1d(x, y)
  newarr = interp_func(np.arange(2.1, 3, 0.1))



x = np.arange(10)
y = x * x


plt.scatter(x, y)
plt.scatter(x, newarr)
plt.show()