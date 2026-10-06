#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

a = float(input("Input A: "))
b = float(input("Input B: "))
c = float(input("Input C: "))

c = c - b

c = c / a

print(c)
