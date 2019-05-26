#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append('src')

from membership_functions import *

# The membership parameters can be modified, if the result
# doesn't satisfy your expectations
gray_membership_function = triangular_membership_function(65, 127, 180)
bright_membership_function = sigma_membership_function(127, 145)
dark_membership_function = inverse_sigma_membership_function(80, 127)

x = np.linspace(0, 255, 1000)
y1 = [gray_membership_function(param) for param in x]
y2 = [bright_membership_function(param) for param in x]
y3 = [dark_membership_function(param) for param in x]


fig, axs = plt.subplots(figsize=(25, 18))
axs.plot(x, y1, x, y2, x, y3)
axs.set_xlabel('Gray Values', fontsize=16)
axs.set_ylabel('Membership', fontsize=16)
axs.set_title("Membership Functions for 8 bit Images", fontsize=18)
axs.grid()

plt.annotate('Gray Membership Function', xy=(127, 1),
             xycoords='data',
             xytext=(-30, +30),
             textcoords='offset points',
             fontsize=16,
             arrowprops=dict(arrowstyle="->", 
             connectionstyle="arc3,rad=.2"))

plt.annotate('Dark Membership Function', xy=(30, 1),
             xycoords='data',
             xytext=(-30, +30),
             textcoords='offset points',
             fontsize=16,
             arrowprops=dict(arrowstyle="->", 
             connectionstyle="arc3,rad=.2"))

plt.annotate('Bright Membership Function', xy=(220, 1),
             xycoords='data',
             xytext=(-30, +30),
             textcoords='offset points',
             fontsize=16,
             arrowprops=dict(arrowstyle="->", 
             connectionstyle="arc3,rad=.2"))


plt.savefig("images/fuzzy_functions.svg")

plt.show()
