# from stt_conversion import voice
# import wikipedia
# from googlesearch import search
# # v = voice()
# # print(v)

  

# query = "how to make biriyani"
  
# for j in search(query, tld="co.in", num=20, stop=5, pause=2): 
#     print(j) 

# wiki = wikipedia.summary(v, sentences= 2)
# print(wiki)

import bs4
import requests

url= "https://www.thecrazyprogrammer.com/2019/03/python-web-scraping-tutorial.html"
data=requests.get(url)
soup=bs4.BeautifulSoup(data.text,'html.parser')
#print(soup.prettify())


for para in soup.find('):
    print(para)

