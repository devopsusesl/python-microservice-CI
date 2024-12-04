from flask import Flask, render_template, redirect, url_for
import os
import requests

app = Flask(__name__)

# Config class for centralizing service URLs
class Config:
    TRENDING_SERVICE_URL = os.getenv("TRENDING_SERVICE_URL", "http://trending-service:5001/trending")
    NEWS_SERVICE_URL = os.getenv("NEWS_SERVICE_URL", "http://news-service:5002/news")
    CATEGORIES_SERVICE_URL = os.getenv("CATEGORIES_SERVICE_URL", "http://categories-service:5003/categories")
    FREEADS_SERVICE_URL = os.getenv("FREEADS_SERVICE_URL", "http://freeads-service:5004/freeads")

app.config.from_object(Config)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/trending")
def trending():
    response = requests.get(app.config['TRENDING_SERVICE_URL'])
    return response.text

@app.route("/news")
def news():
    response = requests.get(app.config['NEWS_SERVICE_URL'])
    return response.text

@app.route("/categories")
def categories():
    response = requests.get(app.config['CATEGORIES_SERVICE_URL'])
    return response.text

@app.route("/freeads")
def freeads():
    response = requests.get(app.config['FREEADS_SERVICE_URL'])
    return response.text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
