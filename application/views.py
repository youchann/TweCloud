from flask import request, redirect, url_for, render_template, flash, abort, \
        jsonify, session, g
import requests
from application.twitter import get_tweets, conbine_tweets
from application.mecab import exclude_br_and_space
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
    conbined_char = conbine_tweets(tweet_list)
    arranged_char = exclude_br_and_space(conbined_char)

    return render_template('show_results.html', arranged_char=arranged_char)