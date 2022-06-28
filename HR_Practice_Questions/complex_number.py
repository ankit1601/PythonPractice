"""
If we convert complex number to its polar coordinate, we find:
: Distance from to origin, i.e.,
: Counter clockwise angle measured from the positive -axis to the line segment that joins

to the origin.

Python's cmath module provides access to the mathematical functions for complex numbers.

r = sqrt(x**2+y**2)
phase = phase(complex number)
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase, sqrt

if __name__ == '__main__':
    c = eval(input())
    r = sqrt(c.real ** 2 + c.imag ** 2)
    ph = phase(c)
    print(r.real)
    print(ph)
