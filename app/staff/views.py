from flask import request, redirect, url_for, render_template, flash, current_app, jsonify
from flask_login import login_user, logout_user, current_user, login_required
import os, json
from werkzeug.utils import secure_filename
from app import db, bcrypt, config,login
from ..staff import staff
from app.auth.models import User


login.login_view = "auth.LoginAccount"


# ===================== ADMIN ONLY ================================== #

@staff.route('/home')
def home():
    return render_template('home.html')
   


# ===================== END ADMIN ONLY ================================== #

@staff.app_template_filter()
def numberFormat(value):
    return format(int(value), ',d')