# Recursion: functions calling themselves

# Functions calling functions
def f():
    g()
    print("f")

def g():
    print("g")

f()

# Functions calling themselves
def hello():
    print("hello")
    hello()

# hello()

# helpful uses: searching files
# We can control the recursion depth
def controlled(level, end_level):
    print("Recursion depth:", level)
    if level < end_level:
        controlled(level + 1, end_level)

controlled(1, 20)

# Factorial

def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total

print(factorial(9))

def recursive_factorial(n):
    if n == 1:
        return n
    elif n == 0:
        return 1
    else:
        return  n * recursive_factorial(n - 1)

print(recursive_factorial(5))