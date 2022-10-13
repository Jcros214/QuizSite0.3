from .getQuestions import QuestionSet, Question, makeQuestions 

class Team():
	def __init__(self, init) -> None:
		self.name = init[0]
		try:
			self.count = int(init[1])
		except:
			self.count = 0
		self.color = '' #= init[2]

class Quiz():
	def __init__(self, team1=('',''), team2=('',''), team3=('','')) -> None:
		questionset = QuestionSet(makeQuestions())
		self.master = ''
		self.team1 = Team(team1)
		self.team2 = Team(team2)
		self.team3 = Team(team3)

		self.leds		=''
		self.switches	=''
		self.statusLed	=''
		self.resetSwitch=''
		
		self.makeHTML()

		self.HTML = f"""
<table>
	<tr>
		{self.leds}
	</tr>
	<tr>
		{self.switches}
	</tr>
	<tr>
		{self.statusLed}
	</tr>
	<tr>
		{self.resetSwitch}
	</tr>
</table>
"""


	def makeHTML(self):
		quizzers = [self.team1.count, self.team2.count, self.team1.count]
		quizzerCtr = 0

		for team in [self.team1, self.team2, self.team3]:
			color = team.color
			# TODO Add style rule to change LED color per team
			if team.count != 0:
				for quizzer in range(team.count):
					quizzerCtr += 1
					self.leds = self.leds + f'<td><span class="led">{quizzer+1}</span></td>'
				self.leds = self.leds + '<td></td>'
				quizzerCtr += 1

			self.switches = self.switches + '<td><label class="switch"><input type="checkbox"><span class="slider"></span></label></td>'*team.count + '<td></td>'
		try:
			place = round(quizzerCtr / 2)
			self.statusLed = '<td></td>'*place + '<td><span class="led"></span></td>'
			self.resetSwitch = '<td></td>'*place + '<td><button class="button"></button></td>'
		except:
			pass
