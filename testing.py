import csv
l1 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
print [x + y for x, y in zip(l1, l1)]
mydict = {}
test = {}
with open("/Users/changye.li/Documents/scripts/traitsPredictor/process/better.csv", "rb") as f:
	reader = csv.reader(f)
	mydict = dict(reader)
print len(mydict)
with open("/Users/changye.li/Documents/scripts/traitsPredictor/process/BillGates.txt", "r") as f:
	row = f.readline().split(",")
	for item in row:
		if item in mydict:
			if item in test:
				test[item].append(mydict[item])
			else:
				test[item] = [mydict[item]]
for k, v in test.items():
	print k, v

	
