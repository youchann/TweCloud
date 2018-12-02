from flask import request, redirect, url_for, render_template, flash, abort, \
        jsonify, session, g
import requests
from application import app
import application.config as config


@app.route('/')
def show_top_page():
    
    return render_template('login.html') 

@app.route('/results')
def show_results(book_id):

    return render_template('show_entries.html')