class Candidate:
	def__init__(self, name, data)

	# after self comes what we might need to know about candidate

	self.candidate = name
	self.data = data.loc[data["endorsee"] == name]

	def countEndorsements(self):
		return len(self.data)

	def getScores(self):
		return self.data["points"]