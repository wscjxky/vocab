import requests
from bs4 import BeautifulSoup


def get_trans(word_spilt):
    print("开始翻译")
    words_trans={}
    for w in word_spilt:
        w = w[0]
        api_url = 'http://apii.dict.cn/mini.php?q=%s' % w
        data = requests.get(api_url)
        if data.status_code == 200:
            data = data.text
            soup = BeautifulSoup(data, 'html.parser')
            body = soup.find('body')
            trans=body.get_text()[len('1Define '):]
            words_trans[w]=trans
    print("翻译完成")
    return words_trans

def get_voice(word_spilt):
    print("获取单词读音")
    for w in word_spilt:
        w = w[0]
        api_url = 'http://dict.youdao.com/dictvoice?audio=%s&le=eng' % w
        data = requests.get(api_url)
        if data.status_code == 200:
            fs = open("%s.mp3" % w, 'wb')
            fs.write(data.content)
            fs.close()
    print("单词读音获取完成")
            # break
