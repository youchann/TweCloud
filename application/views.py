import os, json
from flask import request, redirect, url_for, render_template, jsonify, \
         session, g, Markup
import application.twitter as twitter
import application.janome as janome
from application.word_cloud import create_wordcloud
from application import app

app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def show_top_page():
	# 際アクセスしても利用できるように
    session.pop('file_name', None)
    session.pop('oauth_token', None)
    session.pop('oauth_token_secret', None)

    to_auth_page_url = twitter.get_request_token()

    return render_template('login.html', url=to_auth_page_url)

@app.route('/analyze', methods=['POST'])
def analyze_tweet():
	
	# callbackURLに付与されるパラメータ
    oauth_token = request.json['oauth_token']
    oauth_verifier = request.json['oauth_verifier']

    access_token = twitter.get_access_token(oauth_token, oauth_verifier)

    tweet_list = twitter.get_tweets(access_token)
    conbined_char = twitter.conbine_tweets(tweet_list)
    arranged_char = janome.exclude_br_and_space(conbined_char)
    analyzed_data = janome.janome_analysis(arranged_char)

    print(analyzed_data)
    session['file_name'] = create_wordcloud(' '.join(analyzed_data)) + '.png'
    session['oauth_token'] = access_token['oauth_token']
    session['oauth_token_secret'] = access_token['oauth_token_secret']

    return_data = {'file_name':session.get('file_name')}
    return jsonify(ResultSet=json.dumps(return_data))


@app.route('/result')
def show_result():
    # file_name = session.get('file_name')

    # image_markup = Markup('<img src="static/images/' + file_name + '">')
    # return render_template('show_result.html', image_markup=image_markup)
    return render_template('show_result.html')


@app.route('/create_share')
def create_share_tweet():
    file_name = session.get('file_name')

    image_markup = Markup('<img src="static/images/' + file_name + '">')
    return render_template('create_share.html', image_markup=image_markup)


@app.route('/end_share', methods=['POST'])
def share_cloud():
	if request.method == 'POST':
		tweet_text = request.form['text']

	oauth_token = session.get('oauth_token')
	oauth_token_secret = session.get('oauth_token_secret')
	file_path = 'application' + url_for('static', filename='images/' + session.get('file_name'))

	twitter.tweet_with_image(oauth_token, oauth_token_secret, tweet_text, file_path)

	return  render_template('end_share.html')