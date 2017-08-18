import re
import string
import pandas as pd
from nltk.corpus import stopwords
class trainBuild:
	def __init__(self):
		self.stop = list(set(stopwords.words("english")))
		self.word  =[] ## NRC word list
		self.better = {} ## NRC word attributes
		self.data = pd.DataFrame() ## all data
	## get all required values
	def getValues(self):
		nrc = pd.read_csv("/Users/changye.li/Documents/scripts/traitsPredictor/process/better.csv", header = None, index_col = False)
		for index, row in nrc.iterrows():
			self.better[row[0]] = row[1:].values.tolist()
			self.word.append(row[0])
		self.data = pd.read_csv("/Users/changye.li/Documents/scripts/traitsPredictor/mypersonality_final.csv")
	## get attribute vectors by status
	def getStatusProcessed(self):
		status = [] ## processed status
		## iterate dataframe by rows
		for index, row in self.data.iterrows():
			s = row["STATUS"]
			attr = []## attribute vectors for each status
			## status process
			s = re.sub(r"(?:@\S*|#\S*|http(?=.*://)\S*)", "", s.rsplit("\n")[0].lower())
			s = s.replace("rt", "").rsplit("\n")[0]
			for word in s.translate(None, string.punctuation).split():
				if(word in self.word and word not in self.stop):
					attr.append(self.better[word])
			status.append([sum(x) for x in zip(*attr)])
		#status = filter(None, status)
		## keep only english status, and clean the .csv file
		label_delete = [i for i, v in enumerate(status) if not v]
		self.data.drop(label_delete, inplace = True)
		## update train dataset
		self.data.to_csv("/Users/changye.li/Documents/scripts/traitsPredictor/clean/trainV1.csv", index = False, header = False)
		mat = [] ## store processed numerical vectors
		for index, row in self.data.iterrows():
			mat.append(status[index] + row[2:].values.tolist())
		## write to file
		pd.DataFrame(mat).to_csv("/Users/changye.li/Documents/scripts/traitsPredictor/clean/trainV2.csv", index = False, header = False)
x = trainBuild()
x.getValues()
x.getStatusProcessed()