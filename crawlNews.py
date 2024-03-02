import requests
from bs4 import BeautifulSoup
import requests
import argparse

import re
def findAuthor(inputString):
    inputString = "這是一個[搜尋這裡]的範例字串"

    # 使用正規表達式搜尋 [ ] 中的子字串
    match = re.search(r'〔(.*?)〕', inputString)

    if match:
        result = match.group(1)
        print("找到的子字串:", result)
    else:
        # print("未找到符合的子字串")
        pass




def crawl_ltn_news(url):
    # 發送GET請求並取得響應
    print(url)
    response = requests.get(url)
    
    # 使用Beautiful Soup解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 獲取新聞標題
    all_h1 = soup.find_all('h1')
    for title in all_h1:
        if title.text != "":
            print (f'{title.text}')
            break
    print("***********************")
    # 獲取新聞內容
    contents=soup.find(class_='text').find_all('p')
    # contents=soup.find_all('p')
    
    # findAuthor(contents[0])

    
    # 印出所有內容
    for content in contents:
        if("請繼續往下閱讀..." in content.text):
            continue
        if("下載APP" in content.text):
            continue
        if("自由時報版權所有不得轉載" in content.text):
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
