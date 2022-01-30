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

def scrapeData(tdData):
    tdData = []
    htmldata = apstrada_lapu("https://www.ss.lv/lv/real-estate/flats/rezekne-and-reg/sell/") 
    soup = BeautifulSoup(htmldata, 'html.parser')
    for item in soup.find_all('td', class_="msga2-o pp6"):
        tdData.append(item)
    return tdData

def scrapeNos(url, filters):
    nosData = []
    nosData2 = []
    tdData = scrapeData("")
    for x in range(0, len(tdData), 7):
        nosData.append(tdData[x])
    for y in nosData:
        tmpString = ""
        tmpString = str(y).replace('<td c="1" class="msga2-o pp6" nowrap="">',"")
        tmpString = tmpString.replace("</td>", "")
        tmpString = tmpString.replace("<b>", "")
        tmpString = tmpString.replace("</b>", "")
        nosData2.append(tmpString)
    return nosData2, tdData

def scrapeM2(url, filters):
    m2Data = []
    m2Data2 = []
    tdData = scrapeData("")
    for x in range(2, len(tdData), 7):
        m2Data.append(tdData[x])
    for y in m2Data:
        tmpString = ""
        tmpString = str(y).replace('<td c="1" class="msga2-o pp6" nowrap="">',"")
        tmpString = tmpString.replace("</td>", "")
        tmpString = tmpString.replace("<b>", "")
        tmpString = tmpString.replace("</b>", "")
        m2Data2.append(tmpString)
    return m2Data2

def scrapeIst(url, filters):
    istData = []
    istData2 = []
    tdData = scrapeData("")
    for x in range(1, len(tdData), 7):
        istData.append(tdData[x])
    for y in istData:
        tmpString = ""
        tmpString = str(y).replace('<td c="1" class="msga2-o pp6" nowrap="">',"")
        tmpString = tmpString.replace("</td>", "")
        tmpString = tmpString.replace("<b>", "")
        tmpString = tmpString.replace("</b>", "")
        istData2.append(tmpString)
    return istData2

def scrapeStavs(url, filters):
    stData = []
    stData2 = []
    tdData = scrapeData("")
    for x in range(3, len(tdData), 7):
        stData.append(tdData[x])
    for y in stData:
        tmpString = ""
        tmpString = str(y).replace('<td c="1" class="msga2-o pp6" nowrap="">',"")
        tmpString = tmpString.replace("</td>", "")
        tmpString = tmpString.replace("<b>", "")
        tmpString = tmpString.replace("</b>", "")
        stData2.append(tmpString)
    return stData2

def scrapeCena(url, filters):
    cenaData = []
    cenaData2 = []
    tdData = scrapeData("")
    for x in range(6, len(tdData), 7):
        cenaData.append(tdData[x])
    for y in cenaData:
        tmpString = ""
        tmpString = str(y).replace('<td c="1" class="msga2-o pp6" nowrap="">',"")
        tmpString = tmpString.replace("</td>", "")
        tmpString = tmpString.replace("<b>", "")
        tmpString = tmpString.replace("</b>", "")
        cenaData2.append(tmpString)
    return cenaData2
