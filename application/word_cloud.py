# coding:utf-8
# %matplotlib inline
import uuid
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def create_wordcloud(text):

    # 環境に合わせてフォントのパスを指定する。
    fpath = "/Library/Fonts//ヒラギノ丸ゴ ProN W4.ttc"

    # ストップワードの設定
    stop_words = [ u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', \
             u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した',  u'思う',  \
             u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て',u'に',u'を',u'は',u'の', u'が', u'と', u'た', u'し', u'で', \
             u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'']

    wordcloud = WordCloud(background_color="white",font_path=fpath, width=900, height=500, \
                          stopwords=set(stop_words)).generate(text)

    plt.figure(figsize=(15,12))
    plt.imshow(wordcloud)
    plt.axis("off")

    file_name = create_file_name() # ランダムなファイル名を生成

    plt.savefig('application/static/images/' + file_name + '.jpg')
    #plt.show()

    return file_name

def create_file_name():
    return str(uuid.uuid1())