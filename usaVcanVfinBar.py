import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
usa = []
can = []
fin = []
with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		else:
			if row[4] == "USA":
				usa.append(row[4])
			elif row[4] == "CAN":
				can.append(row[4])
			elif row[4] == "FIN":
				fin.append(row[4])

print('total medals for CAN:', len(can))
print('total medals for USA:', len(usa))
print('total medals for FIN:', len(fin))

print('processed', line_count, 'row of data')


name_list = ['USA', 'CAN', 'FIN']
num_list = [len(usa),len(can),len(fin)]
plt.bar(range(len(num_list)), num_list, tick_label = name_list, color = 'rgb')
plt.title("Medal won by USA, CAN and FIN (Bar)")
plt.show()