import csv
import matplotlib.pyplot as plt

with open('data/Libraries_-_2017_Computer_Sessions_by_Location.csv') as f:
    reader = csv.reader(f) # make a reader object
    data = list(reader) # casting the reader object as a list

names = [x[0] for x in data][1:] # all chi library names (alphabetical)
name_index = [x for x in range(len(names))]
print(name_index)

print(data)
ytd = [x[-1] for x in data][1:]
ytd = [int(x) for x in ytd] # year to date computer sessions for libraries
print(ytd)

# plot ytd vs library as a bar graph
plt.figure(1, figsize=(16, 8), tight_layout=True)
plt.bar(name_index, ytd)
plt.xticks(name_index, names, rotation=90, fontsize=8) # indexed list, strings as list
plt.ylabel("Computer Sessions")
plt.title("Public Library Computer Sessions in Chicago During 2017", fontsize=20)
plt.show()