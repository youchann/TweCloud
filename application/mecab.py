

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

    return char

# 改行を除外
def exclude_br_and_space(char):
    char = char.replace('\n','')
    char = char.replace(' ', '')
    print('改行の削除完了')
    return exclude_url(char)