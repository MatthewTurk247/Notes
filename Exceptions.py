# Exceptions
import math

# Divide by zero error
x = 5

try:
    print(x/0)
except:
    print('you can\'t divide by zero')

# Value error
try:
    x = int("A")
except:
    print('value error: looking for an integer')

# # File and IOErrors
try:
    my_file = open('my_file.txt')
except:
    print('directory does not exist')

# Print out your error (great for debugging)

try:
    5/0
except Exception as e:
    print(e)

# MPG calculator
done = False

while not done:
    try:
        miles = float(input("Enter the miles: "))
        gallons = float(input("Enter the gallons: "))
        print(miles/gallons, 'MPG')
        done = True
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print("This always prints at the end")
        # Useful if you need to close a file or state that a process is done...you could also just do it out of the loop
# NumPy

# Built-in clean up using WITH
with open('data/villains.txt') as f:
    for line in f:
        print(line.strip())

# now you don't have to do clean and stuff and this is safe and compact!
# Better than D'Aloisio

# thus automatically closes the file when completed

# HIGH SCORE
my_score = 100

try:
    with open('data/high_score.txt', 'r') as f:
        for line in f:
            high_score = int(line.strip())
    if my_score > high_score:
        with open('data/high_score.txt', 'w') as f:
            f.write(my_score)
except Exception as e:
    f = open('data/high_score.txt', 'w')
    f.write(str(my_score))
    f.close()