from flask import Flask
from flask import render_template, make_response
from modules import dataScraper
from flask import url_for
from flask import render_template, make_response
from flask import request
import os

app = Flask(__name__)

@app.route('/')
def index():
    pictures = dataScraper.scrapeImg("","")
    nosaukumi = dataScraper.scrapeNos("","")
    m2 = dataScraper.scrapeM2("","")
    ist = dataScraper.scrapeIst("","")
    stavs = dataScraper.scrapeStavs("","")
    cena = dataScraper.scrapeCena("","")
    garums = len(pictures)
    if not request.cookies.get('language'):
        res = make_response('Set language')
        res.set_cookie('language', 'latvian')
        return render_template("indexLV.html",pictures=pictures,nosaukumi=nosaukumi,m2=m2,ist=ist,stavs=stavs,cena=cena,garums=garums)
    else:
        language = request.cookies.get('language')
        if language=='latvian':
            return render_template("indexLV.html",pictures=pictures,nosaukumi=nosaukumi,m2=m2,ist=ist,stavs=stavs,cena=cena,garums=garums)
        else:
            return render_template("indexEN1.html",pictures=pictures,nosaukumi=nosaukumi,m2=m2,ist=ist,stavs=stavs,cena=cena,garums=garums)

@app.route('/karte')
def raditKarti():
    language = request.cookies.get('language')
    if language=='latvian':
        return render_template("karteLV.html")
    else:
        return render_template("karteEN.html")

@app.route('/toppied')
def toppied():
    pictures = dataScraper.scrapeImg("","")
    nosaukumi = dataScraper.scrapeNos("","")
    m2 = dataScraper.scrapeM2("","")
    ist = dataScraper.scrapeIst("","")
    stavs = dataScraper.scrapeStavs("","")
    cena = dataScraper.scrapeCena("","")
    garums = len(pictures)
    language = request.cookies.get('language')
    if language=='latvian':
        return render_template("toppiedLV.html",pictures=pictures,nosaukumi=nosaukumi,m2=m2,ist=ist,stavs=stavs,cena=cena,garums=garums)
    else:
        return render_template("toppiedEN.html",pictures=pictures,nosaukumi=nosaukumi,m2=m2,ist=ist,stavs=stavs,cena=cena,garums=garums)

@app.route('/parmums')
def parmums():
    language = request.cookies.get('language')
    if language=='latvian':
        return render_template("parmumsLV.html")
    else:
        return render_template("parmumsEN.html")

@app.route('/health')
def health():
  return "OK"

if __name__ == '__main__':
  app.run(debug="true")
