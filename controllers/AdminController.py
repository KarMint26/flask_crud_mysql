from flask import render_template, request, redirect, url_for, flash
from models import db, Students

def index_dashboard():
    return render_template('admin/dashboard.html')

def users_dashboard():
    return render_template('admin/users.html')