import requests
from bs4 import BeautifulSoup
import requests
import argparse
import json

import re
def findAuthor(inputString):
    # inputString = "這是一個[搜尋這裡]的範例字串"
    # print(inputString)
    beg = inputString.find("〔")
    end = inputString.find("／")
    # print(beg ,end)
    author=inputString[beg+3:end]
    
    # 使用正規表達式搜尋 [ ] 中的子字串
    # author = re.search(r'記者(.*?)／', inputString)

    if author:
        # result = match.group(1)
        # print("找到的子字串:", result)
        return author
    else:
        # print("未找到符合的子字串")
        return ""




def crawl_ltn_news(url,returnJson):

    # returnJson={}
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

            # if json file value don't want title
            # just commit this line
            returnJson["title"]=title.text
            
            break
    print("***********************")
    # 獲取新聞內容
    contents=soup.find(class_='text').find_all('p')
    time = soup.find(class_="time")
    print(time.text.strip())
    returnJson["createDatetime"]=time.text.strip()
    # contents=soup.find_all('p')
    # try:
    #     findAuthor(contents[1].text)
    # except IndexError:
    #     pass

    
    # 印出所有內容
    text=""
    for content in contents:

        # remove garbage text
        if("請繼續往下閱讀..." in content.text):
            # print(contents.index(content))
            contents.remove(content)
            continue
        if("下載APP" in content.text):
            # print(contents.index(content))
            contents.remove(content)
            continue
        if("自由時報版權所有不得轉載" in content.text):
            # print(contents.index(content))
            contents.remove(content)
            continue
        # print(content.text)
        text+=content.text
    author=findAuthor(text)
    print(author)
    if(author):
        returnJson["author"]=author
    else:
        returnJson["author"]=' '
        
    returnJson["source"]='自由時報'
    returnJson["content"]=text
    # print(returnJson)
    print("========================================")



    
if __name__ == "__main__":
    
    parser=argparse.ArgumentParser()
    parser.add_argument("--url",type=str)
    args=parser.parse_args()
    
    # 指定要爬取的自由時報新聞分類或頁面的URL
    
    url = args.url
    # 調用爬蟲函數
    jsonDict={}
    crawl_ltn_news(url, jsonDict)
