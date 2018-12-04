from flask import request, redirect, url_for, render_template, flash, abort, \
        jsonify, session, g
import requests
from application.getTweets import get_tweets
from application import app

@app.route('/')
def show_top_page():

    return render_template('login.html')

@app.route('/results', methods=['GET', 'POST'])
def analyze_tweets():

    # idを取得
    if request.method == 'POST':
        twitter_id = request.form['id']
	
    tweet_list = get_tweets(twitter_id)

    return render_template('show_results.html', tweet_list=tweet_list)