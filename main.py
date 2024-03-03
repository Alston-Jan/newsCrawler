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
    # news = html.select('[href]')
    # print(news)
    return news

if __name__ == "__main__":
    categories=getCategories()
    news=[]


    #print all types of news
    for i in range(len(categories)):
        print(f'{i}: {categories[i].text}')
    
    # select news by number
    select=int(input("please enter the type of news: "))


    try:
        allNews=get_all_news(categories[select].get('href'))

        #display all news in the selected type
        for i in range(len(allNews)):
            print(f"{i} {allNews[i].text}")

        news=allNews[int(input("please select the news: "))]
        crawl_ltn_news(news.get('href'))
    except AttributeError:
        print(f"{select} {categories[select]}: format not support")        
