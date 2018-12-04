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

        # jsonデータからツイートを取得
        for tweet in timeline:
            tweet_list.append(tweet['text'])
        tweet_list.pop(-1) # 最後の要素を削除(次のループで追加されるため)

        while True: # max_idが一番古いIDになるまで繰り返す
            print('%d番目のリクエスト' % loop_count, max_id)
            new_tweet_list = []

            params['max_id'] = max_id # paramsの更新
            req = twitter.get(url, params=params)

            timeline = json.loads(req.text)
            new_max_id = timeline[-1]['id']

            # jsonデータからツイートを取得
            for tweet in timeline:
                new_tweet_list.append(tweet['text'])

            if max_id != new_max_id:
                new_tweet_list.pop(-1) # 最後の要素を削除(次のループで追加されるため)
                tweet_list.extend(new_tweet_list)
                max_id = new_max_id
                loop_count += 1
            else:
                tweet_list.extend(new_tweet_list)
                break

        # ループ終了後
        print('取得ツイート数', len(tweet_list))
        return tweet_list
    else:
        print("ERROR: %d" % req.status_code)