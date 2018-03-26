import csv
import matplotlib.pyplot as plt

with open('data/Libraries_-_2017_Computer_Sessions_by_Location.csv') as f:
    reader = csv.reader(f) # make a reader object
    data = list(reader) # casting the reader object as a list

names = [x[0].strip() for x in data][1:] # all chi library names (alphabetical)
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
# plt.show()

# plot three libraryies
headers = data.pop(0)
print(headers)
print(names)
print(names.index('Lincoln Park'))
print(names.index("Lincoln Belmont"))
print(names.index("Sulzer Regional"))

month_names = headers[1:-1]
print(month_names)

month_numbers = [x for x in range(12)]
sulzer_y = data[names.index("Sulzer Regional")][1:-1]
sulzer_y = [int(x) for x in sulzer_y]
lb_y = data[names.index("Lincoln Belmont")][1:-1]
lb_y = [int(x) for x in lb_y]
lp_y = data[names.index("Lincoln Park")][1:-1]
lp_y = [int(x) for x in lp_y]

plt.figure(2)
plt.plot(month_numbers, sulzer_y, label="Sulzer")
plt.plot(month_numbers, lb_y, label="Lincoln and Belmont")
plt.plot(month_numbers, lp_y, label="Lincoln Park")
plt.ylabel("Computer Sessions")
plt.xticks(month_numbers, month_names, rotation=80)
plt.legend(bbox_to_anchor=(0.75, 0.40), loc="center")
# why....just why
plt.title("Computer Users/Month (2017)")
plt.show()