import random

# Loop Notes

# FOR LOOPS

for i in range(10):
    print("Python")

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(5, 50, 3):
    print(i)

for i in range(100, -1, -5):
    print(i)

# IF STATEMENT
x = 4
if x > 10:
    print("x is greater than 5")
elif x > 5:
    print("X is greater than 10 (won't run)")

# RANDOM NUMBERS
print(random.randrange(10))  # random int 0 from to 9
print(random.randrange(10, 20))
print(random.randrange(5, 101, 5))
print(random.random)  # float from 0 to directly underneath 1
print(random.random() * 5 + 5)

# BREAK
# automatically exits from the nearest loop (that you're currently inside)
for i in range(100):
    print(i)
    if i > 50:
        break

for i in range(10000):
    n = random.randrange(1000)
    if n == 0:
        print(i)
        break

# FOR ELSE - if you complete the FOR loop, you do the else
for i in range(1000):
    n = random.randrange(1000)
    if n == 0:
        print(i)
        break
else:
    print("Else statement triggered")

# CONTINUE - Ends current iteration and skips to the next iteration of the loop. It doesn't leave the loop.
for i in range(100):
    n = random.randrange(100)
    if n % 2 == 0:
        continue
    print(n)  # skipped over for odd numbers
