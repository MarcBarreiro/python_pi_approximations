from math import sqrt


iterations = 1000000
result = 0
for i in range(1, iterations):
    result += 6/i**2

print(sqrt(result))