# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 11:39:16 2019
@author: lakeh
"""
#import smtplib
#import requests
#from bs4 import BeautifulSoup
#from datetime import date
#import json
from website_specific_scrapers import *
from send_email import send_email
#from .send_email.py import send_email

credentials = "C:\\Users\\lakeh\\Documents\\proj\\news_scraper_credentials.txt"

def scrape_and_send(scrapers):
    articles = str()
    recipients = ['lakeheckaman@gmail.com']
    for scrape in scrapers:
        temp_articles = scrape()
        articles += temp_articles
    send_email(articles, credentials, recipients)
  
news_scrapers = [scrape_AlJazeera, scrape_PoliticoEU, scrape_SCMP, scrape_WSJ, scrape_BBC]
scrape_and_send(news_scrapers)
