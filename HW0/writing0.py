# -*- coding: utf-8 -*-
"""
AMATH 301
Homework 0 - Writeup code

Created on Fri Oct  2 11:58:05 2020

@author: chase
"""

import numpy as np
import matplotlib.pyplot as plt

# Problem 1: Straight Line
x = np.arange(-5,5+0.5,0.5)
y = x
plt.plot(x, y, color='black')
plt.plot(x, y, color='blue', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Problem 2: Parabola
x = np.arange(-5, 5 + 0.5, 0.5)
y = x**2
plt.plot(x, y, color = 'black')
plt.plot(x, y, marker = 'o', color = 'blue')
plt.xlabel('x')
plt.ylabel('y')