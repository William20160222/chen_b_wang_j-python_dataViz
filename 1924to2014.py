import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
medal_in_1924 = []
medal_in_1948 = []
medal_in_1972 = []
medal_in_2002 = []
medal_in_2014 = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print('stripping out categories')
			categories.append(row)
			line_count += 1
		else:
			if row[0] == "1924":
				medal_in_1924.append(row[0])
			elif row[0] == "1948":
				medal_in_1948.append(row[0])
			elif row[0] == "1972":
				medal_in_1972.append(row[0])
			elif row[0] == "2002":
				medal_in_2002.append(row[0])
			elif row[0] == "2014":
				medal_in_2014.append(row[0])

print('total medals in 1924:', len(medal_in_1924))
print('total medals in 1924:', len(medal_in_1948))
print('total medals in 1924:', len(medal_in_1972))
print('total medals in 1924:', len(medal_in_2002))
print('total medals for 2014:', len(medal_in_2014))

print('processed', line_count, 'row of data')

name_list = ['1924', '1948', '1972', '2002', '2014']
num_list = [len(medal_in_1924),len(medal_in_1948),len(medal_in_1972),len(medal_in_2002),len(medal_in_2014)]
plt.bar(range(len(num_list)), num_list, tick_label = name_list)
plt.title("total medals issued by time")
plt.show()





