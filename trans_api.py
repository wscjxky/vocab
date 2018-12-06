import requests
from bs4 import BeautifulSoup


def get_trans(word_spilt):
    print(word_spilt)
    for w in word_spilt:
        w = w[0]
        api_url = 'http://apii.dict.cn/mini.php?q=%s' % w
        print(api_url)
        data = requests.get(api_url)
        if data.status_code == 200:
            data = data.text
            soup = BeautifulSoup(data, 'html.parser')
            body = soup.find('body')
            print(body.get_text())
            break


def get_voice(word_spilt):
    print(word_spilt)
    for w in word_spilt:
        w = w[0]
        api_url = 'http://dict.youdao.com/dictvoice?audio=%s&le=eng' % w
        print(api_url)
        data = requests.get(api_url)
        if data.status_code == 200:
            fs = open("temp.mp3", 'wb')
            fs.write(data.content)
            fs.close()
            print(data)
            break
