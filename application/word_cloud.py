import uuid
from wordcloud import WordCloud

def create_wordcloud(text):

    # 環境に合わせてフォントのパスを指定する。
    fpath = "/app/.fonts/rounded-mplus-1c-regular.ttf"

    # ストップワードの設定
    stop_words = [ u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', \
             u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した',  u'思う',  \
             u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て',u'に',u'を',u'は',u'の', u'が', u'と', u'た', u'し', u'で', \
             u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'']

    wordcloud = WordCloud(background_color="white",font_path=fpath, width=1080, height=607, \
                          stopwords=set(stop_words)).generate(text)

    file_name = create_file_name() # ランダムなファイル名を生成
    wordcloud.to_file('/app/application/static/clouds/' + file_name + '.png')

    return file_name

def create_file_name():
    return str(uuid.uuid1())