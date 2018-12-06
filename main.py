import trans_api
import ppl
import parse_doc
if __name__ == '__main__':
    url = r"C:\Users\Administrator\Desktop\paper\paper\A study of the impact of Corporate Social Responsibility and price image on retailer personality and consumers0 reactions (satisfaction, trust and loyalty to the retailer).pdf"
    url=r"https://www.researchgate.net/profile/Samer_Madanat/publication/277663164_Simultaneous_Netw" \
        r"ork_Optimization_Approach_for_Pavement_Management_Systems/links/5571ca1108aeacff1ff91668/" \
        r"Simultaneous-Network-Optimization-Approach-for-Pavement-Management-Systems.pdf?origin=homeFee" \
        r"d_download&_iepl%5BviewId%5D=4L3DTh8DOKWgQwlbO6R4A9zZ&_iepl%5BsingleItemViewId%5D=FP1ReD2YO7g" \
        r"0vvAq5093WAj8&_iepl%5BpositionInFeed%5D=1&_iepl%5BhomeFeedVariantCode%5D=nu&_iepl%5Bactivity" \
        r"Id%5D=948248823078913&_iepl%5BactivityType%5D=person_add_bookmark_publication&_iepl%5Bactivit" \
        r"yTimestamp%5D=1520521337&_iepl%5Bcontexts%5D%5B0%5D=homeFeed&_iepl%5BinteractionType%5D=publicatio" \
        r"nDownload"
    result = parse_doc.parsepdf(url)
    print(result)
    # text='Zielke, S., 2008. Exploring asymmetric effects in the formation of retail price'
    words_spilt=ppl.get_words_top(text=result,top=5)
    print(words_spilt)
    result=trans_api.get_trans(words_spilt)
    print(result)
    trans_api.get_voice(words_spilt)
