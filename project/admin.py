# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from . models import User
from . import db

admin = Blueprint('admin', __name__) 

@admin.route('/admin')  
@admin.login_required
def admin():
    
    return render_template('admin.html')
