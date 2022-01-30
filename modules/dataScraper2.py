from pip._vendor import requests
from bs4 import BeautifulSoup

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

def scrapeNos(url, filters):
    nosData = []
    nosData2 = []
    tdData = []
    htmldata = apstrada_lapu("https://www.ss.lv/lv/real-estate/flats/rezekne-and-reg/sell/") 
    soup = BeautifulSoup(htmldata, 'html.parser')
    for item in soup.find_all('td', class_="msga2-o pp6"):
        tdData.append(item)
    for x in range(0, len(tdData), 7):
        nosData.append(tdData[x])
    for y in nosData:
        tmpString = ""
        tmpString = str(y).replace('<td c="1" class="msga2-o pp6" nowrap="">',"")
        tmpString = tmpString.replace("</td>", "")
        tmpString = tmpString.replace("<b>", "")
        tmpString = tmpString.replace("</b>", "")
        nosData2.append(tmpString)
    return nosData2

print(scrapeNos("", ""))
