# Lists

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