# main.py


from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@main.route('/material')
@login_required
def material():
    style = """\
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

    print('\n\n', request.args)
    try:
        if request.args['words']=='true':
            style = """\
                <style>
dt {
display: inline-block;
}
</style>
"""
            return render_template('material.html', style=style)
    except:
        pass
    return render_template('material.html', style=style)
        
@main.route('/quiztracker')
@login_required
def quizTracker():
    return render_template('quiztracker.html')
        
