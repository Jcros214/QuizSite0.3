# Backend
import random
from time import sleep
import os

class Question():
	def __init__(self, question: str, answer: str, reference: str, type: str) -> None:
		self.q = question.strip()
		self.a = answer.strip()
		self.r = reference.strip()
		try:
			self.book = self.r[:2]
			# self.chapter = self.r[3:self.r.find(':')]
			self.chRef = self.r[:self.r.find(':')]
		except:
			pass


		self.t = type

class QuestionSet():
	def __init__(self, questions) -> None:
		self.questions = questions
		self.randomQuestions = self.questions
		random.shuffle(self.randomQuestions)
		self.quizset = self.getQuestions(20, '1C 12')
	
	def quiz(self, question: Question):
		print(question.q)
		input()
		print(question.a)
		print(question.r,'\n')
	
	# get a set number of questions from specified chapter
	def getQuestions(self, count: int, chapter: list) -> list:
		# if type(chapter) != type(str):
		# 	raise ValueError
		output = list()
		for question in self.randomQuestions:
			if question.chRef in chapter:
				output.append(question)
			if len(output) >= count:
				break
		return output		


path = 'QuizSite0.3/project/static/txt/i-iiCOR.txt'

def makeQuestions():
	with open(path, 'r') as file:
		rawQuestions = file.readlines()

	questions = list()
	q = ''
	a = ''
	t = ''
	r = ''
	for lineNum in range(int(len(rawQuestions))):
		line = rawQuestions[lineNum]

		if (lineNum) % 3 == 0:
			t = line[0]
			qStart = line.find('.\t')+2
			q = line[qStart:-1]
			pass
		elif (lineNum+2) % 3 == 0:
			refLoc = [
				line.find('[')+1,
				line.find(']')
			]
			
			r = line[refLoc[0]:refLoc[1]]
			a = line[refLoc[1]+2:]
		elif (lineNum+1) % 3 == 0:
			questions.append(Question(q,a,r,t))
			q = ''
			a = ''
			t = ''
			r = ''

	return questions


# questions = QuestionSet(makeQuestions())
# questions = questions.getQuestions(26, ['1C 15', '1C 16', '2C 1', '2C 2'])
# for question in questions:
# 	# print(question.q)

# # print(questions)