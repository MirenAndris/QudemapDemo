from flask import Flask
from flask import requestpip
from flask import url_for
from flask import render_template, make_response
from modules import dataScraper
import os

app = Flask(__name__)

@app.route('/')
def root():
    #pictures = dataScraper.scrapeData("url","filters")
    return render_template("index.html")#, pictures=pictures)

@app.route('/karte')
def raditKarti():
    return render_template("karte.html")

@app.route('/health')
def health():
  return "OK"

if __name__ == '__main__':
  app.run(debug="true")
