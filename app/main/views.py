from flask import render_template, redirect, url_for, request
from . import main
from ..models import User
from flask_login import login_required


@main.route('/')
# @login_required
def home():

    return render_template('home.html')