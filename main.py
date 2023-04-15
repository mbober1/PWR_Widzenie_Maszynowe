#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
# from scipy.interpolate import interp1d

# weż jakąś funkcję np x^2 

# interpolacja NN i interpolacja liniowa
# interpolacja scipy
# interpolacja wielomianem 3 i 4 stopnia
# porównać wyniki MSE (mean squared error) oraz czas wykonania

# def interpolation_scipy(x, y, x_target):
#   y_interp = interp1d(x, y)
#   newarr = interp_func(np.arange(2.1, 3, 0.1))


zero_order = lambda x : 0 + (x > -0.5) + (x < 0.5) # NN
first_order = lambda x : 0 + (1 - abs(x)) * (abs(x) < 1) # liniowa


x = np.arange(10)
x2 = np.arange(0, 10, 0.1)
y = x * x


plt.scatter(x, y)
plt.scatter(x2, zero_order(x))
plt.scatter(x2, first_order(x))
plt.show()




# Interpolacja wielomianem

y = ax^2 + bx + c # wielomian drugiego stopnia

y1 = ax1^2 + b * x1 + c
y2 = ax2^2 + b * x2 + c
y3 = ax3^2 + b * x3 + c
# bierzemy 3 punkty, podstawiamy i rozwiązujemy układ. Dostajemy A, B i C. 

y = ax^3 + bx^2 + cx + d 
# cztery róœniania i 4 punkty



# Porównaj te 4 metody do siebie. Użyj także tych w SCIFY

