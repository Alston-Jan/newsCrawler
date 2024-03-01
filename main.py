from bs4 import BeautifulSoup
import requests
from crawlNews import crawl_ltn_news

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
    news = html.find(class_='list').find_all(class_='tit')
    return news
    # print(categories)
    # for i in categories:
    #     print(i.get('href'))
    #     print(i.text)

if __name__ == "__main__":
    categories=getCategories()
    news=[]
    for i in len(categories):
        print(f'{i}: {categories[i]}')
    select=input("please enter the type of news: ")
    allNews=get_all_news(categories[select].get('href'))
    for news in allNews:
        
        # print(news.text)
        # print(news.get('href'))
        crawl_ltn_news(news.get("href"))
        
