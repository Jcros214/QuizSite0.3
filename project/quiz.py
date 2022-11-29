from flask import Blueprint, redirect, request, render_template, session

quiz = Blueprint('quiz', __name__)

from .static.python.getQuestions import QuestionSet, Question, makeQuestions, allCh
from .static.python.quiz import Quiz


# A decorator used to tell the application
# which URL is associated function
@quiz.route('/quiz')
def quizpage():
    active_quiz = Quiz().load_json(session["quiz"])



@quiz.route('/practice', methods=["GET", "POST"])
def practice():
    if request.method == "GET":
        return render_template('quiz/practice_questions.html')
    else:
        try:
            global chs, prac_questions
            chs = [chapter.strip() for chapter in request.form["chapters"].split(',')]
            prac_questions = global_questionset.getQuestions(50, chs)
            return render_template('quiz/practice_questions.html')
        except:
            return redirect('/')
        



@quiz.route('/quiz/nextquestion')
def nextquestion():
    # TMP!
    # Future implemntation:
        # Include filters to limit the kind of question that can be returned
    return f'<a style="text-align: center;" hx-get="/quiz/nextanswer" hx-swap="outerHTML">Question:<br>{prac_questions[questionctr].q}</a>'

@quiz.route('/quiz/nextanswer')
def nextanswer():
    global questionctr
    # TMP!
    # Future implemntation:
        # Include filters to limit the kind of question that can be returned
    ques = prac_questions[questionctr].q
    ans  = prac_questions[questionctr].a
    questionctr += 1
    return f'<a style="text-align: center;" hx-get="/quiz/nextquestion" hx-swap="outerHTML">Question:<br>{ques}<br><br><br><br>Answer:<br>{ans}</a>'

