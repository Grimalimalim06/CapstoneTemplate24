from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Distraction
from app.classes.forms import DistractionForm
from flask_login import login_required
import datetime as dt

# Create a new distraction
@app.route('/distraction/new', methods=['GET', 'POST'])
@login_required
def distractionNew():
    form = DistractionForm()
    if form.validate_on_submit():
        newDistraction = Distraction(
            grade=form.grade.data,
            distracted=form.distracted.data,
            difficulty=form.difficulty.data,
            phoneusage=form.phoneusage.data,
            modify_date=dt.datetime.utcnow() 
        )
        newDistraction.save()
        return redirect(url_for("view_distraction", distractionID=newDistraction.id))  

    return render_template("distractionform.html", form=form)

# Edit an existing distraction
@app.route('/distraction/edit/<distractionID>', methods=['GET', 'POST'])
@login_required
def distractionEdit(distractionID):
    form = DistractionForm()
    editDistraction = Distraction.objects.get(id=distractionID) 

    if form.validate_on_submit():
        editDistraction.update(
            grade=form.grade.data,
            distracted=form.distracted.data,
            difficulty=form.difficulty.data,
            phoneusage=form.phoneusage.data,
            modify_date=dt.datetime.utcnow()  
        )
        return redirect(url_for("view_distraction", distractionID=distractionID))  


    form.grade.process_data(editDistraction.grade)
    form.distracted.process_data(editDistraction.distracted)
    form.difficulty.process_data(editDistraction.difficulty)
    form.phoneusage.process_data(editDistraction.phoneusage)

    return render_template("distractionform.html", form=form)  


@app.route('/distraction/<distractionID>')
@login_required
def view_distraction(distractionID):
    distraction = Distraction.objects.get(id=distractionID)  
    return render_template("distraction.html", distraction=distraction)


@app.route('/distractions')
@login_required
def distractions():
    allDistractions = Distraction.objects() 
    return render_template("distractions.html", distractions=allDistractions)


@app.route('/distraction/delete/<distractionID>')
@login_required
def distractionDelete(distractionID):
    delDistraction = Distraction.objects.get(id=distractionID)  
    delDistraction.delete()
    distractions=Distraction.objects()
    return render_template('distractions.html', distractions=distractions)