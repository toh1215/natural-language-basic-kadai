# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:21:50 2024

@author: user
"""

import re
from bs4 import BeautifulSoup
from urllib import request

url = "https://www.aozora.gr.jp/cards/000148/files/2371_13943.html"
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()

print(soup)

main_text = soup.find("div", class_="main_text")
print(main_text)

tags_to_delete = main_text.find_all(["rp", "rt"])
for tag in tags_to_delete:
    tag.decompose()
print(main_text)

main_text = main_text.get_text()
print(main_text)    

main_text = re.sub(r"[\u3000 \n \r]", "", main_text)
print(main_text)
#%%
url = "http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt"
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()
print(soup)

stopwords_text = soup.text
print(stopwords_text)
stopwords_list = stopwords_text.split("\r\n")
stopwords_list = [word for word in stopwords_list if word]
print(stopwords_list)

split_text_list = ["近頃", "は", "大分", "方々", "の", "雑誌", "から", "談話", "を", "しろしろ", "と", "責め", "られ", "て", "、 ", "頭", "が", "がらん胴", "に", "なっ", "た", "から", "、", "当分", "品切れ", "の", "看板", "でも", "懸か", "け", "たい", "くらい", "に" ,"思っ", "て", "いま", "す", "。"]
result_text_list = list()
for split_text in split_text_list:
    if split_text in split_text_list:
        result_text_list.append(split_text)

print(result_text_list)





