import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
jpn = []
kor = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		else:
			if row[4] == "JPN":
				jpn.append(row[4])
			elif row[4] == "KOR":
				kor.append(row[4])

print('total medals for JPN:', len(jpn))
print('total medals for KOR:', len(kor))

print('processed', line_count, 'row of data')

total = len(jpn) + len(kor)
jpn_percentage = int(len(jpn) / total * 100)
kor_percentage = int(len(kor) / total* 100)


labels = "JPN", "KOR"
sizes = [jpn_percentage, kor_percentage]
colors = ['yellow', 'green']
explode = (0.1, 0.1)
plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=180)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Medal won by jpn and kor")
plt.xlabel("")
plt.show()