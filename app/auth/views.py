from flask import request, redirect, url_for, render_template, flash
from flask_login import login_user, logout_user, current_user
from app import db, bcrypt
from ..auth import auth
from ..admin import admin
from ..staff import staff
from app.auth.forms import RegistrationForm, LoginForm, ResetPasswordForm
from app.auth.models import User


@auth.route('/register', methods=['GET','POST'])
def RegisterAccount():
    """Register new staff only"""
    if current_user.is_authenticated:
        return redirect(url_for('staff.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name= form.first_name.data, last_name=form.last_name.data ,my_id=form.ID.data, active=False, is_admin=False)    
        user.set_password(form.password.data)    
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.LoginAccount'))
    else:
        print(form.errors)
    return render_template('register.html', form=form, url=request.path)

@auth.route('/admin/register', methods=['GET','POST'])
def RegisterAdminAccount():
    """Register new admin account only"""
    if current_user.is_authenticated:
        return redirect(url_for('admin.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name= form.first_name.data,last_name= form.last_name.data,my_id=form.ID.data, active=False, is_admin=True)    
        user.set_password(form.password.data)    
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.LoginAdminAccount'))
    else:
        print(form.errors)
   
    return render_template('register.html', form=form, url=request.path)

@auth.route('/login', methods=['GET','POST'])
def LoginAccount():
    """Signing in staff only"""
    print(request.url)
    if current_user.is_authenticated:
        return redirect(url_for('staff.home'))
    
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(my_id=form.ID.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.LoginAccount'))
        login_user(user, remember=form.remember_me.data)
        user.active = True
        db.session.commit()
        
        return redirect(url_for('admin.home'))
    return render_template('login.html', form=form, url=request.path)

@auth.route('/admin/login', methods=['GET','POST'])
def LoginAdminAccount():
    """Login Admin only"""
    print(request.url)

    if current_user.is_authenticated:
        return redirect(url_for('admin.home'))
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(my_id=form.ID.data).first()
        if user is None or not user.check_password(form.password.data) or not user.is_admin:
            flash('Invalid username or password')
            return redirect(url_for('auth.LoginAdminAccount'))
        login_user(user, remember=form.remember_me.data)
        user.active = True
        db.session.commit()
        return redirect(url_for('admin.home'))
    return render_template('login.html', form=form, url=request.path)

@auth.route('/logout')
def logout():
    id = current_user.id 
    user = User.query.get(id)
    user.active=False
    db.session.commit()
    logout_user()
    return redirect(url_for('auth.LoginAccount'))

@auth.route('/admin/logout')
def admin_logout():
    id = current_user.id 
    user = User.query.get(id)
    user.active=False
    db.session.commit()
    logout_user()
    return redirect(url_for('auth.LoginAdminAccount'))

@auth.route('/resetpassword')
def reset_password():
    form=ResetPasswordForm()
    return render_template('forgot.html', form=form)

@auth.route('/admin/resetpassword')
def admin_reset_password():
    form=ResetPasswordForm()
    return render_template('forgot.html', form=form)
        




