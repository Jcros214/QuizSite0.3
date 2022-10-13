globQuiz seems to be reset on each call of quizpage()


```python

from .static.python.quiz import Quiz as quizClass

globQuiz = quizClass()

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
 
```

```
Note: 	ImmutableMultiDict is request.form
		<project.static.python.quiz.Quiz object...> is the variable in question

...

7.0.0.1 - - [13/Oct/2022 01:11:08] "GET /quiz HTTP/1.1" 200 -

...
 
ImmutableMultiDict([('fname', 'abc123'), ('Team1name', 'Team1'), ('Team1count', '5'), ('Team2name', 'Team2'), ('Team2count', '5'), ('Team3name', 'Team3'), ('Team3count', '5')]) 
 

<project.static.python.quiz.Quiz object at 0x106e2aad0>
127.0.0.1 - - [13/Oct/2022 01:11:09] "POST /quiz HTTP/1.1" 200 -
...
 
ImmutableMultiDict([('action', 'next')]) 
 

<project.static.python.quiz.Quiz object at 0x106ed2a70>
127.0.0.1 - - [13/Oct/2022 01:11:10] "POST /quiz HTTP/1.1" 200 -
...
```