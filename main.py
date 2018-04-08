
import timeit
import os

os.system("make")

import example


def normal_power(base, exponent):

	lbase = base

	for _ in range(1, exponent):

		base = base * lbase

	return base


def pythonic_power(base, exponent):

	return base ** exponent


timepower = timeit.timeit(lambda:   normal_power(2, 300), number = 100000)
pypower   = timeit.timeit(lambda: pythonic_power(2, 300), number = 100000)
ipower    = timeit.timeit(lambda: example.ipower(2, 300), number = 100000)
fpower    = timeit.timeit(lambda: example.fpower(2, 300), number = 100000)
dpower    = timeit.timeit(lambda: example.dpower(2, 300), number = 100000)

print()

# These first 5 tests denote how quickly all of these functions were able to
# calculate (2^300) 100k times. (in seconds)
print(timepower)
print(pypower)
print(ipower)
print(fpower)
print(dpower, "\n")

# These 4 tests denote how many times faster the latter function is
# compared to timepower(the non-pythonic function written in python)
print(timepower / pypower)
print(timepower / ipower)
print(timepower / fpower)
print(timepower / dpower, "\n")

# These 3 tests denote how fast the integer, float and double variations of the
# power templated function are compared to the pythonic function written in 
# Python. (1 being exactly as fast, 0.5 being half as fast)
print(pypower / ipower)
print(pypower / fpower)
print(pypower / dpower)
