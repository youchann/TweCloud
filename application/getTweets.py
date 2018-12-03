import json
from requests_oauthlib import OAuth1Session
import application.config as config

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

def get_tweets(screen_name):
    loop_count = 0
    max_id = None
    tweet_list = []
    params = {
        'count': 200,
        'screen_name': screen_name,
        'max_id': None,
        'exclude_replies': True,
        'include_rts': False
    }
    req = twitter.get(url, params=params)

    # ツイートを取得
    if req.status_code == 200:
        timeline = json.loads(req.text)
        max_id = timeline[-1]['id'] # 最後のツイートIDを取得

        while True: # max_idが一番古いIDになるまで繰り返す
            print('%d番目のリクエスト' % loop_count, max_id)

            params['max_id'] = max_id
            req = twitter.get(url, params=params)

            append_timeline = json.loads(req.text)
            new_max_id = append_timeline[-1]['id']

            if max_id != new_max_id:
                timeline = timeline + append_timeline
                max_id = new_max_id
                loop_count += 1
            else:
                break

        print('取得ツイート数', len(timeline))
        for tweet in timeline:
            tweet_list.append(tweet['text'])
        return tweet_list
    else:
        print("ERROR: %d" % req.status_code)