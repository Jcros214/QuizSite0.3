from flask import Blueprint, redirect, request, render_template

quiz = Blueprint('quiz', __name__)

from . import quizClass, global_questionset
from .static.python.getQuestions import QuestionSet, Question, makeQuestions, allCh

questionset = QuestionSet(makeQuestions())
quizset = questionset.getQuestions(25, allCh)
questionNum = 0



# A decorator used to tell the application
# which URL is associated function
@quiz.route('/quiz', methods =["GET", "POST"])
def quizpage():
    global globQuiz
    
    if request.method == "GET": return render_template('newquiz.html')
    print('\n', '\n', request.form, '\n', '\n')

    if request.method == "POST":
        if request.form.get('action'): # posted from question advance buttons
            global questionNum 
            if request.form.get('action') == 'back':
                # User hit 'back'
                questionNum -= 1
            elif request.form.get('action') == 'next':
                # User hit 'next'
                questionNum += 1
            else:
                raise ValueError("Action was invalid.")

            if questionNum < 1 or questionNum > 20:
                questionNum = 0
                item = Question("Hit Next to start quiz", '', '', '')
            else:
                item = quizset[questionNum-1]
            print("DebugA:", globQuiz)

            return render_template('quiz.html', quiz=globQuiz, num=questionNum, curQues=item)
            # global Quiz
            
            # return render_template("quiz.html", quiz=Quiz, curQues=Question("Hit Next to start quiz", '', '', ''))

        else: # posted from newquiz.html
            team1_name = request.form.get("Team1name")
            team2_name = request.form.get("Team2name")
            # team3_name = request.form.get("Team3name")

            team1_count = request.form.get("Team1count")
            team2_count = request.form.get("Team2count")
            # team3_count = request.form.get("Team3count")

            # global Quiz
            globQuiz = quizClass((team1_name, team1_count),(team2_name, team2_count))
            print("DebugB:",globQuiz)
            return render_template("quiz.html", quiz=globQuiz, curQues=Question("Hit Next to start quiz", '', '', ''))
 

# @quiz.route("/question/<prog>", methods=['GET', 'POST'])
# def items(prog=None):

@quiz.route('/activequizzes')
def activequizzes():
    return redirect('/')


@quiz.route('/practice')
def practice():
    return render_template('quiz/practice_questions.html')

questionctr = 0

@quiz.route('/quiz/nextquestion')
def nextquestion():
    # TMP!
    # Future implemntation:
        # Include filters to limit the kind of question that can be returned
    return f'<a hx-get="/quiz/nextanswer" hx-swap="outerHTML">Question:<br>{global_questionset.questions[questionctr].q}</a>'

@quiz.route('/quiz/nextanswer')
def nextanswer():
    global questionctr
    # TMP!
    # Future implemntation:
        # Include filters to limit the kind of question that can be returned
    ques = global_questionset.questions[questionctr].q
    ans  = global_questionset.questions[questionctr].a
    questionctr += 1
    return f'<a hx-get="/quiz/nextquestion" hx-swap="outerHTML">Question:<br>{ques}<br><br><br><br>Answer:<br>{ans}</a>'

