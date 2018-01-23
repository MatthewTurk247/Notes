# What if I fall? Oh, but what if I fly?
# MATH

#floats vs ints
print(1.2/2 + 1.2) # lol the binary screwed up
my_float = 1.2/2 + 1.2
print(int(my_float)) # chops off any remainder (like floor division)

my_int = 123
print(float(my_int)) # notice the decimal

snake_case = "lower case with underscores between words. like camel case but python rules"
print(snake_case)
camelCase = "JavaScript and Swift use this"

# do not do the following
# no spaces
# no special characters
# no decimals, that's for attributes/methods of classes (dot notation)
# no numbers to start the variable name, but ball8 for instance is ok

#Assignment
my_variable = 8
x, y = (3, 4) # a tuple (immutable list)
print(x)
print(y)

# MATH OPERATIONS
# + - * /
# **
# //
# %

# COMPOUND ASSIGNMENT OPERATORS
# +- -= *= /=
x = 5
x += 1
print(x)
x *= 3
x **= 0.5 # sqrt(x)
print(x)

# ROUND
print(round(x, 3))

# FORMAT
# well take this a bit slowly for a week, start getting used to the software, we'll look at a git tomorrow,
# create notes repository

# "{}".format()

# Let's format some text
first = "Jerry"
last = "Garcia"
print(first, last)
print(first + last)
print("{}".format(first))
print("{} {}".format(first, last))
# We'll look at the chicago crime database!!!
# why don't people use full screen
# this first week is going painfully slow
print("First: {}\tLast: {}".format(first,last))

# d for digit/int, f for float, e for exponent to force a format
pi = 3.1415926535897
print("{:.3}".format(pi))
# {.3f} rounds up to 3
print("{:+}".format(pi))

# put commas
my_number = 190238102
print("{:,}".format(my_number))

# right align :>xd where x is the width of the text
print("{:>20}".format(first))
# center align
print("{:^20}".format(first))
# typer shark
# percentage {:%} {:.2}
# scientific notation {:e} {:.2e}
print("{:.2e}".format(2338972983468980317401983))
avogadros_number = 6.022e23
# leading zero for other (or other placeholder, I suppose) {:05}
print("{:0002}".format(243))
# don't screw up
print("${:.2f}".format(142.3))