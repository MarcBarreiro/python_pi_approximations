# https://en.wikipedia.org/wiki/Vi%C3%A8te%27s_formula
from math import sqrt


iterations = 1000000
result = 1
factor = sqrt(2)
for _ in range(iterations):
    result *= factor/2
    factor = sqrt(2+factor)

pi = 2 / result
print(pi)
