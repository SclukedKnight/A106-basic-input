#! python3
#
# Find the radius of a sphere if you are given the volume.
# Think about how you would need to solve this equation if you were doing it on paper
#
# Inputs:
# Volume (float)
#
# Outputs:
# radius (float)
#
# Test output Volume of 20.22 should give radius of:1.69002229118
# Note: You will need to do some strange things with your cube root.
# Remember that a cube root is the same as an exponent of 1/3, but
# here you will need to do a power of 1.0/3 or something strange happens.

import math

v = float(input("Please input volume of sphere: "))
unit = str(input("I need units in order to know what I'm doing, please enter unit character: "))

v = v / (4 / 3)
v = v / math.pi
v = v ** (1.0 / 3)
print(f"Volume of the sphere is {v} {unit}")