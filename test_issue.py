# app/routes/about.py

from flask import Blueprint, render_template

about_bp = Blueprint('about', __name__)

COMPANY_INFO = {
    "name": "TechCorp",
    "description": "Welcome to our Company! We build great software.",
    "founded_year": 2015
}

@about_bp.route('/about')
def about_us():
    return render_template('about.html', info=COMPANY_INFO)