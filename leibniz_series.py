# https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
# 1 - 1/3 + 1/5 - 1/7 + 1/9... = pi/4

iterations = 1000000
result = 0
sign = +1
for i in range(1, iterations, 2):
    result += sign / i
    sign = -sign
pi = 4 * result
print(pi)
