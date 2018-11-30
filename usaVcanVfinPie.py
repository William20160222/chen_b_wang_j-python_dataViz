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

total = len(can) + len(usa)
usa_percentage = int(len(usa) / total * 100)
can_percentage = int(len(can) / total * 100)
fin_percentage = int(len(fin) / total * 100)


labels = "USA", "CAN", "FIN"
sizes = [usa_percentage, can_percentage, fin_percentage]
colors = ['lightblue', 'blue', 'lightgreen']
explode = (0.1, 0.1, 0.15)
plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Medal won by USA, CAN and FIN (Pie)")
plt.xlabel("")
plt.show()