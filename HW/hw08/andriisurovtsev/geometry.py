# geometry
from math import pi, pow

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return pi * pow(radius, 2)