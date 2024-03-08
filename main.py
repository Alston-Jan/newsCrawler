from bs4 import BeautifulSoup
import requests
from crawlNews import crawl_ltn_news
import json

def getCategories():
    url='https://www.ltn.com.tw/'
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    categories = html.find(class_='useMobi').find_all('a')
    categories.pop(24)
    categories.pop(23)
    categories.pop(22)

    return categories
    
def get_all_news(url:str):
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    news = html.find(class_='list').find_all(class_='tit',limit=3)
    # news = html.select('[href]')
    # print(news)
    return news

if __name__ == "__main__":
    categories=getCategories()
    news=[]


    #print all types of news
    for i in range(len(categories)):
        try:
            print(f'{i}: {categories[i].text}')
            allNews=get_all_news(categories[i].get('href'))

        #display all news in the selected type
            for i in range(len(allNews)):
                newsJson={}
                print(f"{i} {allNews[i].text}")
                crawl_ltn_news(allNews[i].get('href'),newsJson)
                news.append(newsJson)

        except AttributeError:
            print(f"{i} {categories[i].get('href')} {categories[i].text}: format not support")        
    with open("output.json","w+",encoding="utf8") as f:
        json.dump(news,f,ensure_ascii=False,indent=4)