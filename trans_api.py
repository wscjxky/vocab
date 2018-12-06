import requests
from bs4 import BeautifulSoup
def get_trans(word_split):

    print(word_split)
    for w in word_split:
        w=w[0]
        api_url = 'http://apii.dict.cn/mini.php?q=%s'%w
        print(api_url)
        data=requests.get(api_url)
        if data.status_code==200:
            data=data.text
            soup = BeautifulSoup(data, 'html.parser')
            body=soup.find('body')
            print(body.get_text())
            break
def get_voice(word_spilt):
