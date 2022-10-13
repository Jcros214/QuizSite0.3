from flask import Blueprint, redirect, request, render_template

quiz = Blueprint('quiz', __name__)

from . import quizClass

from .static.python.getQuestions import QuestionSet, Question, makeQuestions

questionset = QuestionSet(makeQuestions())
quizset = questionset.quizset
questionNum = 0

globQuiz = quizClass()

# A decorator used to tell the application
# which URL is associated function
@quiz.route('/quiz', methods =["GET", "POST"])
def quizpage():
    global globQuiz
    
    if request.method == "GET": return render_template('newquiz.html')
    print('\n', '\n', request.form, '\n', '\n')

    if request.method == "POST":
        if request.form.get('back') or request.form.get('next'): # posted from question advance buttons
            global questionNum 
            if request.form.get('back'):
                # User hit 'back'
                questionNum -= 1
            else:
                # User hit 'next'
                questionNum += 1

            if questionNum < 1 or questionNum > 20:
                questionNum = 0
                item = Question("Hit Next to start quiz", '', '', '')
            else:
                item = quizset[questionNum-1]
            print(globQuiz)
            return render_template('quiz.html', quiz=globQuiz, num=questionNum, curQues=item)
            # global Quiz
            
            # return render_template("quiz.html", quiz=Quiz, curQues=Question("Hit Next to start quiz", '', '', ''))

        else: # posted from newquiz.html
            team1_name = request.form.get("Team1name")
            team2_name = request.form.get("Team2name")
            team3_name = request.form.get("Team3name")

            team1_count = request.form.get("Team1count")
            team2_count = request.form.get("Team2count")
            team3_count = request.form.get("Team3count")

            # global Quiz
            globQuiz = quizClass((team1_name, team1_count),(team2_name, team2_count),(team3_name, team3_count))
            print(globQuiz)
            return render_template("quiz.html", quiz=globQuiz, curQues=Question("Hit Next to start quiz", '', '', ''))
 

# @quiz.route("/question/<prog>", methods=['GET', 'POST'])
# def items(prog=None):

@quiz.route('/activequizzes')
def activequizzes():
    return redirect('/')