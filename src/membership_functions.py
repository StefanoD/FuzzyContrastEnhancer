#!/usr/bin/env python3

import numpy as np


def triangular_membership_function(triangle_start, triangle_peak, triangle_end):
    def membership_function(parameter):
        if parameter < triangle_start:
            return 0

        if triangle_start <= parameter and parameter < triangle_peak:
            return (parameter - triangle_start) / (triangle_peak - triangle_start)

        if triangle_peak <= parameter and parameter < triangle_end:
            return 1 - (parameter - triangle_peak) / (triangle_end - triangle_peak)

        # triangle_end <= parameter
        return 0

    return membership_function


def sigma_membership_function(sigma_start, sigma_end):
    def membership_function(parameter):
        if parameter < sigma_start:
            return 0

        if sigma_start <= parameter and parameter < sigma_end:
            return (parameter - sigma_start) / (sigma_end - sigma_start)

        # sigma_end <= parameter
        return 1

    return membership_function


def inverse_sigma_membership_function(sigma_start, sigma_end):
    def membership_function(parameter):
        if parameter < sigma_start:
            return 1

        if sigma_start <= parameter and parameter < sigma_end:
            return 1 - (parameter - sigma_start) / (sigma_end - sigma_start)

        # sigma_end <= parameter
        return 0

    return membership_function
