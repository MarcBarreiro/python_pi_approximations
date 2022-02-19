# https://en.wikipedia.org/wiki/Wallis_product

iterations = 1000000
result = 1
for i in range(2, iterations, 2):
    result *= i**2/((i-1)*(i+1))

pi = 2 * result
print(pi)
