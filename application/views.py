import os
from flask import request, redirect, url_for, render_template, \
         session, g, Markup
import application.twitter as twitter
import application.janome as janome
from application.word_cloud import create_wordcloud
from application import app

app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def show_top_page():

    to_auth_page_url = twitter.get_request_token()

    return render_template('login.html', url=to_auth_page_url)

@app.route('/analyze')
def analyze_tweet():
    session.pop('file_name', None)

	# callbackURLに付与されるパラメータ
    oauth_token = request.args.get('oauth_token')
    oauth_verifier = request.args.get('oauth_verifier')

    access_token = twitter.get_access_token(oauth_token, oauth_verifier)

    tweet_list = twitter.get_tweets(access_token)
    conbined_char = twitter.conbine_tweets(tweet_list)
    arranged_char = janome.exclude_br_and_space(conbined_char)
    analyzed_data = janome.janome_analysis(arranged_char)
	
    print(analyzed_data)
    session['file_name'] = create_wordcloud(' '.join(analyzed_data))
    return redirect(url_for('show_result')) # パラメータを消すためにリダイレクト


@app.route('/result')
def show_result():
    file_name = session.get('file_name')
    session.pop('file_name', None)

    image_markup = Markup('<img src="static/images/' + file_name + '.jpg">')
    return render_template('show_result.html', image_markup=image_markup)