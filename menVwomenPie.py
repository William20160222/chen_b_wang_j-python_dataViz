import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
men = []
women = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		else:
			if row[5] == "Men":
				men.append(row[5])
			elif row[5] == "Women":
				women.append(row[5])

print('total medals for men:', len(men))
print('total medals for women:', len(women))

print('processed', line_count, 'row of data')

total = len(men) + len(women)
men_percentage = int(len(men) / total * 100)
women_percentage = int(len(women) / total * 100)


labels = "Men", "Women"
sizes = [men_percentage, women_percentage]
colors = ['lightblue', 'pink']
explode = (0.1, 0.1)
plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=180)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Medal won by men and women(Pie)")
plt.xlabel("")
plt.show()