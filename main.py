
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
print(timepower)
print(pypower)
print(ipower)
print(fpower)
print(dpower, "\n")

print(timepower / pypower)
print(timepower / ipower)
print(timepower / fpower)
print(timepower / dpower, "\n")

print(pypower / ipower)
print(pypower / fpower)
print(pypower / dpower)
