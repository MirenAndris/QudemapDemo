import requests
from bs4 import BeautifulSoup
import re

def apstrada_lapu(url):
    r = requests.get(url)
    return r.text

def scrapeImg(url, filters):
    imgData = []
    htmldata = apstrada_lapu("https://www.ss.lv/lv/real-estate/flats/rezekne-and-reg/sell/") 
    soup = BeautifulSoup(htmldata, 'html.parser') 
    for item in soup.find_all('img'):
        txt = item['src']
        if txt[-3:len(txt)] == "jpg" or txt == "https://i.ss.lv/img/buy/homes.lv.gif" or txt == "https://i.ss.lv/img/n.home.gif?v=2":
            imgData.append(txt)
    return imgData