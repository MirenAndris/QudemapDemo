from pip._vendor import requests
from bs4 import BeautifulSoup

def apstrada_lapu(url):
    r = requests.get(url)
    return r.text

def scrapeImg(url, filters):
    imgData = []
    htmldata = apstrada_lapu("https://www.ss.lv/lv/real-estate/flats/rezekne-and-reg/") 
    soup = BeautifulSoup(htmldata, 'html.parser') 
    for item in soup.find_all('img'):
        txt = item['src']
        if txt[-3:len(txt)] == "jpg" or txt == "https://i.ss.lv/img/buy/homes.lv.gif" or txt == "https://i.ss.lv/img/n.home.gif?v=2":
            imgData.append(txt)
    return imgData

def scrapeNos(url, filters):
    nosData = []
    txt = ""
    htmldata = apstrada_lapu("https://www.ss.lv/lv/real-estate/flats/rezekne-and-reg/") 
    soup = BeautifulSoup(htmldata, 'html.parser')
    tdclass = soup.find_all('td', class_="msga2-o pp6")
    for tr in soup.find_all('tbody'):
      for tdclass in tr:
        txt = soup.find_all('<b>')

    return txt

print(scrapeNos("", ""))
