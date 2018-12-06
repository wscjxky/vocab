import nltk
import re
from zhon.hanzi import punctuation
import string
filtered_sentence = []


def get_words_sort(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    result = sorted(result.items(), key=lambda x: x[1],reverse=True)
    return result


def get_words_top(text):
    stop_words = nltk.corpus.stopwords.words('english')
    stop_words.append('the')
    text = re.sub(r"[%s]+" % punctuation, "", text)
    text = re.sub(r"[%s]+" % string.punctuation, "", text)
    text = re.sub(r"[\d]+", "", text)
    text = text.lower()
    print(text)
    word_tokens = nltk.word_tokenize(text)
    word_split = []
    for w in word_tokens:
        if len(w) > 2 and w not in stop_words:
            word_split.append(w)

    return get_words_sort(word_split)






