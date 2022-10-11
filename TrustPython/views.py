"""
Routes and views for the flask application.
"""

from datetime import datetime
from logging import makeLogRecord
from flask import render_template, make_response
from TrustPython import app
import requests
import hashlib

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

# load in the bundled CA for this specific request
@app.route("/requests")
def call_requests():
    r = requests.get("https://untrusted-root.badssl.com", verify='badssl.crt')
    resp = make_response(hashlib.sha256(r.text.encode('utf-8')).hexdigest().upper(),200)
    resp.mimetype = "text/plain"
    return resp

# so you see what it looks like
@app.route("/fail_request")
def fail_request():
    r = requests.get("https://untrusted-root.badssl.com")
    resp = make_response(hashlib.sha256(r.text.encode('utf-8')).hexdigest().upper(),200)
    resp.mimetype = "text/plain"
    return resp

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='TrustPython'
    )
