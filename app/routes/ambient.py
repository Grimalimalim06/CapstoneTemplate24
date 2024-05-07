from app import app
from flask_login.utils import login_required
from flask import render_template, redirect, flash, url_for
from app.classes.data import User
from app.classes.forms import ProfileForm
from flask_login import current_user


@app.route('/ambient')
def ambient_music():
    return render_template('ambient.html')  
