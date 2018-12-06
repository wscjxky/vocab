import trans_api
import ppl
import parse_doc
if __name__ == '__main__':
    # url = r"C:\Users\Administrator\Desktop\paper\paper\A study of the impact of Corporate Social Responsibility and price image on retailer personality and consumers0 reactions (satisfaction, trust and loyalty to the retailer).pdf"
    # result = parsepdf(url)
    text='Zielke, S., 2008. Exploring asymmetric effects in the formation of retail price'
    words_spilt=ppl.get_words_top(text)
    print(words_spilt)
    # result=trans_api.get_trans(words_spilt)
    result=trans_api.get_voice(words_spilt)

    print(result)