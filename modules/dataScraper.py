from bs4 import BeautifulSoup
import requests
import re

#pievienot beautifulsoup4 pie requirements.txt GitHubā

def apstrada_lapu(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def scrapeData(url, filters):
    data = []
    imgURLdata = []	
    html = apstrada_lapu("https://www.ss.lv/lv/real-estate/flats/rezekne-and-reg/")

    data = html.find_all('img', class_="isfoto foto_list")
    for row in data:
        imageURL = re.findall('<img.*?src="(.*?)"[^>]+>/g',row)
        imgURLdata.append(imageURL)
    return imgURLdata

#scrapeData ("","")