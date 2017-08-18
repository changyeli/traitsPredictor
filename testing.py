import csv
l1 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
print [x + y for x, y in zip(l1, l1)]

with open(self.root +self.better, "w") as f:
			writer = csv.writer(f)
			for k, v in self.feature.iteritems():
				writer.writerow([k] + v)
with open('dict.csv', 'rb') as csv_file:
    reader = csv.reader(csv_file)
    mydict = dict(reader)

