from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm,UpdateProfile,PitchForm
from ..models import User,Pitche
from flask_login import login_required,current_user
from .. import db

@main.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''
    all_pitches =Pitche.query.all()
    title = 'Home'
    return render_template('index.html', title = title,all_pitches=all_pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/pitch/new' ,methods=['GET','POST'])
@login_required
def create_pitches():
    form = PitchForm()
    if form.validate_on_submit():
        category=form.category.data
        content=form.content.data
        new_pitch = Pitche(content=content,category=category, user=current_user)
        new_pitch.save_pitch()
        # pitch=form.pitch.data

        return redirect(url_for('main.index'))

    return render_template('pitch.html',form =form)     

