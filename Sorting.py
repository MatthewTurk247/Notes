# SORTING
import random

# hungarian selection sorting dance

# Swap values
a = 1
b = 2
print(a, b)
temp = a
a = b
b = temp

print(a, b)
a, b = b, a # pythonic way (the way pythonistas do it)
print(a, b)

# Selection Sort
rando_list = [random.randrange(1,100) for x in range(100)]
print(rando_list)

def selection_sort(l):
    for cur_pos in range(len(l)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(l)):
            if l[scan_pos] < l[min_pos]:
                min_pos = scan_pos
        l[cur_pos], l[min_pos] = l[min_pos], l[cur_pos]

selection_sort(rando_list)
print(rando_list)

# Insertion Sort
rando2 = [random.randrange(1, 100) for x in range(100)]

for key_pos in range(1, len(rando2)):
    key_value = rando2[key_pos]
    scan_pos = key_pos - 1  # look to the dancer on the left
    while (scan_pos >= 0) and (rando2[scan_pos] > key_value):
        rando2[scan_pos + 1] = rando2[scan_pos]
        scan_pos -= 1

    # now everything is shifted to make room for the key_value
    rando2[scan_pos + 1] = key_value

print(rando2)