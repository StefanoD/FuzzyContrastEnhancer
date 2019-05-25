#!/usr/bin/env python3

import numpy as np
from matplotlib.pyplot import imread
from matplotlib.pyplot import imsave

import sys
sys.path.append('src')

from fuzzy_contrast_enhancer import *


image = imread("images/Einstein.tif")
enhanced_image = enhance_grayscale_8bit_image(image)

imsave("images/EnhancedEinstein.png", enhanced_image, cmap='gray')
