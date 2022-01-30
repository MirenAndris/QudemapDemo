from flask import Flask
from flask import render_template, make_response
from modules import dataScraper
from modules import dataScraper2
from flask import url_for
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
    apvDati = dataScraper2.datuApvien("","")
    return render_template("index.html",pictures=pictures,nosaukumi=nosaukumi,m2=m2,ist=ist,stavs=stavs,cena=cena,apvDati=apvDati)

@app.route('/karte')
def raditKarti():
    return render_template("karte.html")

@app.route('/toppied')
def toppied():
    return render_template("toppied.html")

@app.route('/parmums')
def parmums():
    return render_template("parmums.html")

@app.route('/health')
def health():
  return "OK"

if __name__ == '__main__':
  app.run(debug="true")
