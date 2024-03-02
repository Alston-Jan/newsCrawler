import requests
from bs4 import BeautifulSoup
import requests
import argparse

def crawl_ltn_news(url):
    # 發送GET請求並取得響應
    response = requests.get(url)
    
    # 使用Beautiful Soup解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 獲取新聞標題
    news_title = soup.find('h1')
    
    print (f'title: {news_title.text}')
    
    # 獲取新聞內容
    contents=soup.find(class_="text").find_all('p')
    
    
    # 印出所有內容
    for content in contents:
        if("請繼續往下閱讀..." in content.text):
            continue
        if("下載APP" in content.text):
            continue
        print(content.text)
    print("========================================")
    
if __name__ == "__main__":
    
    parser=argparse.ArgumentParser()
    parser.add_argument("--url",type=str)
    args=parser.parse_args()
    
    # 指定要爬取的自由時報新聞分類或頁面的URL
    
    url = args.url
    # 調用爬蟲函數
    crawl_ltn_news(url)
