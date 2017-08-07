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


## data processing
def process(self):
	## user ID
	uid = set(self.data["AUTHID"].values.tolist())
	tokens = []
	## subset original dataset
	k1 = self.data[self.data["AUTHID"] == "b7b7764cfa1c523e4e93ab2a79a946c4"]
	s1 = k1["STATUS"].values.tolist()
	#print k1.iloc[0] ## select row
	for each in s1:
		temp = [w for w in nltk.word_tokenize(each.translate(None, string.punctuation).lower())]
		x = [w for w in temp if w in self.voca]
		tokens.append(x)
	print tokens
	temp = []
	for each in tokens:
		attr = [0]*10
		if len(each) == 0:
			temp.append(attr)
		else:
			for item in each:
				attr = [x + y for x, y in zip(attr, self.dic[item])]
			temp.append(attr)
	print temp
	print [sum(x) for x in zip(*temp)]
