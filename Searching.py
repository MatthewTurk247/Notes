# Searching
import re

file = open("data/villains.txt", "r")

for line in file:
    print(line.strip())

file.close()

file = open("data/villains.txt")

for line in file:
    print("Hello,", line.strip())

file.close()

'''
# We can also write to a file
file = open('data/villains.txt', 'w')
# overwrites entire file

file.write('Lee The Merciless')

file.close()
'''

# appending to a file
'''file = open('data/villains.txt', 'a')
file.write('\nLee the Merciless')
file.close()'''

# Read a file into an array
file = open('data/villains.txt') # the default mode is 'r'
villains = []

# Linear Search

for name in file:
    villains.append(name.strip())

file.close()
key = "Vladimir Noire"
print(villains)
# print(villains.index(key))
i = 0
while i < len(villains) and villains[i] != key:
    i += 1

if i < len(villains):
    print(key, "is at position", i)
else:
    print(key, 'is not found')

# Binary Search

key = 'Morgiana the Shrew'
for i in range(20):
    print(2 ** i)

lower_bound = 0
upper_bound = len(villains) - 1

found = False
middle_pos = 0

while not found and lower_bound <= upper_bound:
    middle_pos = (upper_bound - lower_bound)//2
    if villains[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif villains[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True

if found:
    print("Found", key, "at position", middle_pos)
else:
    print(key, "not found")

# This function takes in a line of text and returns a list of words in the line
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open('data/villains.txt')
all_words = []

for line in file:
    words = split_line(line)
    for word in words:
        all_words.append(word)

print(all_words)
# change