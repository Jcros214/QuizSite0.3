# main.py


import json
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .static.python.getQuestions import QuestionSet, makeQuestions

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@main.route('/material')
# @login_required
def material():
    letterstyle = """\
        <style>
            dt {
                visibility: hidden;
                display: inline-block;
                font-size: 0;
            }
            dt::first-letter {
                visibility: visible;
                font-size: 20pt;
            }
            dt:hover {
                visibility: visible;
                font-size: 20pt;
            }
        </style>
"""
    wordstyle = """\
        <style>
            dt {
                font-size: 20;
                display: inline-block;

            }
        </style>
"""
    qletterstyle = """\
        <style>
            dt {
                visibility: hidden;
                display: inline-block;
                font-size: 0;
            }
            dt::first-letter {
                visibility: visible;
                font-size: 20pt;
            }
            dt:hover {
                visibility: visible;
                font-size: 20pt;
            }
            .noquote {
                display: none;
            }
            </style>
"""
    qwordstyle = """
        <style>
            dt {
                font-size: 20;
                display: inline-block;

            }
            .noquote {
                display: none;
            }

        </style>
    """
    style = {
        'letters':  letterstyle,
        'words':    wordstyle,
        'qletters': qletterstyle,
        'qwords':   qwordstyle,
        None: wordstyle
    }

    return render_template('material.html', style=style[request.args.get('disp')])

@main.route('/quiztracker')
# @login_required
def quizTracker():
    questions = QuestionSet(makeQuestions())
    questions = questions.getQuestions(26, ['1C 15', '1C 16', '2C 1', '2C 2'])
    # questions = {
    #   {questions}
    # }
    # 
    questionset = list()
    questionctr = 1
    for question in questions:
        questionset.append({"questioncounter":questionctr, "type":question.t, "question":question.q, "reference":question.r, "answer":question.a})
        questionctr +=1



    outputQuestions = json.dumps(questionset, indent=4)
    print(outputQuestions)
    # print(questions)
    return render_template('quiztracker.html', questionset=outputQuestions, q1=questionset[0]['question'], a1=questionset[0]['answer'], r1=questionset[0]['reference'], t1=questionset[0]['type'])
