import random


# This function returns whether a point is inside the circle of unit radius
# with center at the origin (0, 0)
def is_inside_circle(x, y):
    return x**2 + y**2 <= 1


# We create 1.000.000 random points inside the square with area = 4
# At each iteration, we update the counter variable adding 1 if the
# point is inside the circle and 0 otherwise.
# Finally, since the relation between areas is circle/square = pi/4 we can isolate pi
if __name__ == '__main__':
    counter = 0
    iterations = 1000000
    for _ in range(iterations):
        counter += is_inside_circle(random.uniform(-1, 1), random.uniform(-1, 1))
    print(4*counter/iterations)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
