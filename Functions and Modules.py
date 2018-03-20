from math import *
# is a wildcard, anything...just imports the whole thing, now instead of math.cos, you can just use cos
# however sometimes you may cause issues when the libraries overlap variable names
from random import randrange
from imports import my_import

# Functions


def my_function(name):
    '''
    Says hello
    :param name:
    :return:
    '''
    print("Hello, {}.".format(name))


def square_cube(n):
    square, cube = n**2, n**3
    return square, cube


if __name__ == "__main__":
    # this is the file that you executed/ran
    my_function("Matthew")
    my_import.product_sum(10, 20)
    print(randrange(100))
    print(pi, e)
    print(log(100000, 10))
    print(square_cube(7)[0], square_cube(7)[1])
    my_function(name="Matthew")

# scope rules:
# python (ex. __main__) - the ones that belong to the language...don't mess with these...
# globals (far left) - can be seen anywhere
# local - ones inside functions, only can be seen locally
# you know all of this...only incompetent simpletons would struggle with this...it's an exercise in logic...
# ionization