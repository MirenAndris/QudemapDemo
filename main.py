from flask import Flask
from flask import request
from flask import url_for
from flask import render_template, make_response
import os

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")

@app.route('/karte',methods = ['POST', 'GET'])
def raditKarti():
    return render_template("karte.html")

@app.route('/health')
def health():
  return "OK"

if __name__ == '__main__':
  app.run(debug="true")
