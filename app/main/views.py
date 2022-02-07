from flask import render_template, redirect, url_for, request
from . import main
from ..models import User



@main.route('/')
def home():

    return render_template('home.html')