# Backend

# All chapters for questions:
allCh = [
	'1C 1',
	'1C 2',
	'1C 3',
	'1C 4',
	'1C 5',
	'1C 6',
	'1C 7',
	'1C 8',
	'1C 9',
	'1C 10',
	'1C 11',
	'1C 12',
	'1C 13',
	'1C 14',
	'1C 15',
	'1C 16',
	'2C 1',
	'2C 2',
	'2C 3',
	'2C 4',
	'2C 5',
	'2C 6',
	'2C 7',
	'2C 8',
	'2C 9',
	'2C 10',
	'2C 11',
	'2C 12',
	'2C 13',	
]

mych = [
	'1C 5',
	'1C 7',
	'1C 12',
	'2C 1'
]

currentch = [
	'2C 5',
	'2C 6'
]

import random
from time import sleep
import os
import json
from pathlib import Path

class Question():
	def __init__(self, question: str, answer: str, reference: str, type: str) -> None:
		self.q = question.strip()
		self.a = answer.strip()
		self.r = reference.strip()
		try:
			self.verse = int(self.r[self.r.find(':')+1:].strip())
		except ValueError:
			self.verse = -1
		try:
			self.book = self.r[:2]
			# self.chapter = self.r[3:self.r.find(':')]
			self.chRef = self.r[:self.r.find(':')]
			
		except:
			pass


		self.t = type

class QuestionSet():
	def __init__(self, questions: list[Question]) -> None:
		self.questions = questions
		self.randomQuestions = self.questions
		random.shuffle(self.randomQuestions)
		self.quizset = None#self.getQuestions(20, '1C 12')
	
	def quiz(self, question: Question, number = ""):
		number = f"{number}.\t" if number else ''
		print(f"{number}{question.q}\nA: [{question.r}] {question.a}\n")
		input()
	
	def quiz_practice(self, question: Question, number = ""):
		number = f"{number}.\t" if number else ''
		print(f"{number}{question.q}\n")
		input()
		print(f"{question.a}\n[{question.r}]\n\n")
	
	# get a set number of questions from specified chapter
	def getQuestions(self, count: int, chapter: list) -> list:
		# if type(chapter) != type(str):
		# 	raise ValueError
		output = list()
		for question in self.randomQuestions:
			chref = question.chRef
			# try:
			# 	verse = question.verse
			# except:
			# 	verse = 11

			if chref in chapter:# and question.verse <= 10:
				output.append(question)
			# if len(output) >= count:
			# 	break
		return output		

	def questionDump(self) -> list[dict]:
		output = []
		for question in self.questions:
			output += [ {
				"question": question.q,
				"type": question.t,
				"reference": question.r,
				"answer": question.a
			} ]
		return output

	def dump_from_chs(self, chs: list[str]):
		output = []
		for question in self.questions:
			if question.chRef in chs:
				output += [ {
					"question": question.q,
					"type": question.t,
					"reference": question.r,
					"answer": question.a
				} ]
		return output



def makeQuestions() -> list[Question]:

	with open(Path('project/static/json/questions.json').absolute(), 'r') as file:
		questions = json.load(file)
		questions: list[dict]
		output = []
		
		# print(json.dumps(questions, indent=4))
		for question in questions:
			output.append( Question(question['question'], question['answer'], question['reference'], question['answer']) )
		
	return output


def makeQuestionsTXT():
	with open(Path('project/static/txt/i-iiCOR.txt').absolute(), 'r') as file:
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

def dumpToJSON():
	ques = QuestionSet(makeQuestions())
	questions = ques.dump_from_chs(['2C 5', '2C 6']) #ques.questionDump()

	with open('project/static/json/questions.json', 'w') as file:
		file.write(json.dumps(questions, indent=4))

def sortJson():
	
	refs = []
	usedQuestions = []
	newQuestions = []
	with open('QuizSite0.3/project/static/json/questions.json', 'r') as file:
		questions = json.load(file)
		questions: list[dict]
	for question in questions:
		if not (question['reference'] in refs):
			refs.append(question['reference'])

	refs.sort()

	for ref in refs:
		for question in questions:
			if question['reference'] == ref:
				if question['question'] not in usedQuestions:
					newQuestions.append(question)
					usedQuestions.append(question['question'])
				

	# assert len(newQuestions) == len(questions)
	with open('QuizSite0.3/project/static/json/questions.json', 'w') as file:
		file.write(json.dumps(newQuestions, indent=4))


def main():
	ques = QuestionSet(makeQuestions())
	print('\n'*5)
	for question in ques.getQuestions(20, currentch):
		ques.quiz(question)



if __name__ == '__main__':
	questions = QuestionSet(makeQuestions())

	with open('project/static/json/2C5-2C6.json', 'w') as file:
		file.write(json.dumps(questions.dump_from_chs(['2C 5', '2C 6']), indent=4))

	# print('\n'*100)
	# questions = QuestionSet(makeQuestions())
	# questionlist = questions.getQuestions(26, currentch)
	# number = 1
	# for question in questionlist:
	# 	questions.quiz_practice(question, number)
	# 	number += 1
