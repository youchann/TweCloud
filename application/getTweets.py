import json
from requests_oauthlib import OAuth1Session
import application.config as config

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)


def get_tweets(screen_name):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    tweet_list = []

    params = {
        'count': 200,
        'screen_name': screen_name,
        'exclude_replies': True,
        'include_rts': False
    }

    req = twitter.get(url, params = params)

    if req.status_code == 200:
        timeline = json.loads(req.text)
        for tweet in timeline:
            tweet_list.append(tweet['text'])
            # print(tweet['user']['name']+'::'+tweet['text'])
            # print(tweet['created_at'])
            # print('----------------------------------------------------')
    else:
        print("ERROR: %d" % req.status_code)
    
    return tweet_list

