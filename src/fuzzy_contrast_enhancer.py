#!/usr/bin/env python3

import numpy as np
from matplotlib.pyplot import imread
from matplotlib.pyplot import imsave

from membership_functions import *


def enhance_grayscale_8bit_image(image):
    """
    Parameters
    ----------
    image : numpy array, gray scale
        image to be manipulated.
    """
    dark_color = 0
    gray_color = 127
    bright_color = 255

    # The membership parameters can be modified, if the result
    # doesn't satisfy your expectations
    gray_membership_function = np.vectorize(
        triangular_membership_function(65, gray_color, 180))
    bright_membership_function = np.vectorize(
        sigma_membership_function(gray_color, 145))
    dark_membership_function = np.vectorize(
        inverse_sigma_membership_function(80, gray_color))

    dark_image_part = dark_membership_function(image)
    gray_image_part = gray_membership_function(image)
    bright_image_part = bright_membership_function(image)

    enhanced_image = (dark_image_part * dark_color +
                      gray_image_part * gray_color +
                      bright_image_part * bright_color) / \
        (dark_image_part + gray_image_part + bright_image_part)

    enhanced_image = enhanced_image.astype(np.uint8)
    return enhanced_image
