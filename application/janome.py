from janome.tokenizer import Tokenizer

# URLを除外
def exclude_url(char):
    count = 0
    while True:
        location_URL = char.find('https://')
        if location_URL != -1:
            url = char[location_URL:location_URL+23]
            char = char.replace(url, '')
            count += 1
            print(url)
            print('%d番目のurl削除' % count)
        else:
            break

    while True:
        location_URL = char.find('http://')
        if location_URL != -1:
            url = char[location_URL:location_URL+22]
            char = char.replace(url, '')
            count += 1
            print(url)
            print('%d番目のurl削除' % count)
        else:
            break

    return char

# 改行・スペースを除外
def exclude_br_and_space(char):
    char = char.replace('\n','')
    char = char.replace(' ', '')
    print('改行の削除完了')
    return exclude_url(char)



def janome_analysis(text):
    output = []
    t = Tokenizer()
    tokens = t.tokenize(text)
    for token in tokens:
        part_of_speech = token.part_of_speech.split(',')[0]
        if part_of_speech in [u'名詞']:
            output.append(token.surface)
    return output