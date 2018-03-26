import matplotlib.pyplot as plt
import csv
import numpy as np

with open('data/World firearms murders and ownership - Sheet 1.tsv') as f:
    reader = csv.reader(f, delimiter='\t')
    data = list(reader)

headers = data.pop(0)
# print(data)
# print(headers)

# Homicide by firearm rate per 100k vs Average firearms per 100 people
# fitness tesk, weapons training, naval academy, Stanford, NASA, jets

homicide_per100k = []
firearm_per100 = []
country_names = []
# no wars, no political unrest, democracies or similar
countries_to_plot = ['United States', 'France', 'England and Wales', 'Sweden', 'Germany', 'Norway', 'Netherlands',
                     'Iceland', 'Canada', 'Japan', 'South Korea', 'China', 'Australia', 'Poland']

for i in range(len(data)):
    if data[i][0] in countries_to_plot:
        try:
            homicide = float(data[i][5])
            firearm = float(data[i][7])
            name = data[i][0]
            country_names.append(name)
            homicide_per100k.append(homicide)
            firearm_per100.append(firearm)
        except:
            print("Failed {}".format(data[i][0]))


print(homicide_per100k)
print(firearm_per100)

plt.figure(1, figsize=(8, 5))
m, b = np.polyfit(firearm_per100, homicide_per100k, 1) # 1 for linear (returns m and b)
x = [0, 100]
y = [m*pt + b for pt in x]
plt.plot(x, y)
print(m, b)
plt.scatter(firearm_per100, homicide_per100k)

for i in range(len(country_names)):
    plt.annotate(country_names[i], xy=(firearm_per100[i], homicide_per100k[i]))

plt.title("World Firearm Deaths")
plt.ylabel("Homicides per 100k population")
plt.xlabel("Firearms per 100 population")
plt.show()