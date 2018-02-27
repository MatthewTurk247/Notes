# Lists
import random

my_list = ["Abe", "Bev", "Cam", "Dan", "Eve", "Flo", "Gus"]
my_num_list = [8, 4, 7, 5, 2, 9]

print(my_list[0]) # single index
print(my_list[0:2]) # multiple items, first oen included, last one not, it assumes 0 before the colon if you put nothing

# copy of a list
my_new_list = my_list
my_list[3] = "Deb"
print(my_new_list)
print(my_list)
# they point to the same location in the memory, need to make a new list
my_new_list = my_list[:]
print(my_new_list)

# 2d list
my_2dlist = [["Abe", 8], ["Bev", 4], ["Cam", 7]]
print(my_2dlist[1][1])

# if in
if "Cam" in my_list:
    print("Cam is on the list")

# list functions
# for strings, order is (sorta) alphabetical
print(min(my_num_list))
print(max(my_num_list))
print(sum(my_num_list))

# list methods
my_list.append("Abe")
print(my_list.count("Abe")) # finds the number of times an item appears
my_list.insert(0, "Evelyn")
print(my_list)
my_list.sort()
print(my_list)
my_num_list.sort()
my_num_list.reverse()
print(my_num_list)

my_list.pop() # pops off the last one, like the opposite of an append
my_list.pop(2)
print(my_list)
first_in_line = my_list.pop(0) # returns the popped value
print(first_in_line)

del my_list[0:2] # ha ha I did it
print(my_list)

print(my_list.index("Flo"))
a = my_list.copy()
print(a)

# add 10 to each item in the list using iteration
'''for i in range(len(my_list)):
    my_list[i] += 10

print(my_list)'''

# make a 2d list that is 10x10
ten_by_ten = list()
for x in range(10):
    for y in range(10):
        my_list.append([x, y])
        print([x,y])

print("OWEFIUHEWIUFHWEFUIIWE", ten_by_ten)

# print every pair
for pair in ten_by_ten:
    print(pair)

for i in range(len(ten_by_ten)):
    for j in range(len(ten_by_ten[i])):
        ten_by_ten[i][j] += 3232

# make a list of numbers from 0 to 99 and print it
num_list = []
for i in range(100):
    num_list.append(i)

# square every item in the previous list and print it
for i in range(len(num_list)):
    num_list[i] **= 2

# show only odd numbers and print it
num_list2 = []
for n in num_list:
    if n % 2 != 0:
        print('odd', n)
        num_list2.append(n)

num_list3 = []
for i in range(100, 1001):
    num_list3.append(i)

my_list4 = []
# do all four at once
for i in range(100):
    num = i**2
    if num % 2 == 1:
        if num >= 100 and num <= 1000:
            my_list4.append(num)
print(my_list4)

# list comprehension
# [returned_item for iterator in range_or_list filter]
my_list5 = [x**2 for x in range(100) if x**2 % 2 == 1 and x**2 >= 100 and x**2 <= 1000]
print(my_list5)

my_rolls = [random.randrange(1, 7) for x in range(101)]
print(my_rolls)
my_rolls = [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(101)]
print(my_rolls)
doubles = [x for x in my_rolls if x[0] == x[1]]
print(doubles)

# we can generate a list and filter doubles on a single line
doubled = [y for y in [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(101)] if y[0] == y[1]]
print(doubles)