# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 11:39:16 2019
@author: lakeh
"""
import smtplib
import requests
from bs4 import BeautifulSoup
import pdfkit
from datetime import date
import json
#from .send_email.py import send_email

def scrape_and_send(scrapers):
    articles = str()
    for scrape in scrapers:
        temp_articles = scrape()
        articles += temp_articles
    send_email(articles)

#set output to either 'text' or 'json'
def scrape_SCMP(output='text'):
    #select url   
    papername = "SCMP"
    url = 'https://www.scmp.com/news'
    #pull data from API
    r1=requests.get(url)
    coverpage = r1.content
    #convert to soup
    soup = BeautifulSoup(coverpage)
    #find the first main article section and then pull all articles that have summaries from this section
    t = soup.find('div', class_="main-article-section-content").find_all('div', class_='article__summary')
    #pull the link, title, summary text from these articles   
    articles=str()
    articles_json = []
    for i in t:
        link = i.parent.find('div', class_='article__title').find('a')['href']
        title = i.parent.find('div', class_='article__title').text
        text = i.text
        #concat it all together
        string = (
                f"{title}.\n"
                f"{text}\n"
                f"https://www.scmp.com{link}\n\n\n"
                )
        articles += string
        article_obj = {
            'title': title, 
            'text': text, 
            'link': link
            }
        articles_json.append(article_obj)
    #write articles to a file and return, depending on output type specified
    if output== 'text':
#        filename = 'C:\\Users\\lakeh\\Documents\\Python Scripts\\' + papername + str(date.today()) + '.txt'
#        with open(filename, 'w') as text_file:
#            print(articles, file=text_file) 
        return articles
    elif output == 'json':
        filename = 'C:\\Users\\lakeh\\Documents\\Python Scripts\\'+ papername + str(date.today()) + '.json'
        with open(filename, 'w') as outfile:
            json.dump(articles_json, outfile) 
        return articles_json
    else: print("""please set output = to 'json' or 'text'""")
      
def scrape_WSJ(output = 'text'):
    #select url   
    papername = "WSJ"
    url = 'https://www.wsj.com/news/markets'
    #pull data from API
    r1=requests.get(url)
    coverpage = r1.content
    #convert to soup
    soup = BeautifulSoup(coverpage)     
               
    #find the first main article section and then pull all articles that have summaries from this section
    t = soup.find('div', class_="lead-story").find_all('h3', class_='wsj-headline')
    #pull the link, title, summary text from these articles   
    articles=str()
    count = 0
    articles_json = []
    for i in t:
        try: 
            count += 1
            link = i.find('a', class_='wsj-headline-link')['href']
            text = i.parent.find('p', class_='wsj-summary').text
            title = i.text
            #concat it all together
            string = (
                    f"{title}.\n"
                    f"{text}\n"
                    f"{link}\n\n\n"
                    )
            articles += string
            article_obj = {
                'title': title, 
                'text': text, 
                'link': link
                }
            articles_json.append(article_obj)
        except:"Nonetype"
    
    #write articles to a file and return, depending on output type specified
    if output== 'text':
#        filename = 'C:\\Users\\lakeh\\Documents\\Python Scripts\\' + papername + str(date.today()) + '.txt'
#        with open(filename, 'w') as text_file:
#            print(articles, file=text_file) 
        return articles
    elif output == 'json':
        filename = 'C:\\Users\\lakeh\\Documents\\Python Scripts\\'+ papername + str(date.today()) + '.json'
        with open(filename, 'w') as outfile:
            json.dump(articles_json, outfile) 
        return articles_json
    else: print("""please set output = to 'json' or 'text'""")

def scrape_BBC(output = 'text'):
    #select url   
    papername = "BBC"  
    url = 'https://www.bbc.com/news'
    #pull data from API
    r1=requests.get(url)
    coverpage = r1.content
    #convert to soup
    soup = BeautifulSoup(coverpage)     
               
    #find the first main article section and then pull all articles that have summaries from this section
    t = soup.find('div', class_="nw-c-top-stories--standard").find_all('div', class_='gs-c-promo-body')
    #pull the link, title, summary text from these articles and store in dict to convert to json
    articles=str()
    articles_json = []
    for i in t:
        link = i.find('a', class_='gs-c-promo-heading')['href']
        text = i.find('p', class_='gs-c-promo-summary').text
        title = i.find('a', class_='gs-c-promo-heading').text
        #concat it all together
        string = (
                f"{title}.\n"
                f"{text}\n"
                f"https://www.bbc.com/{link}\n\n\n"
                )
        articles += string
        #store into dict for json
        article_obj = {
                'title': i.find('a', class_='gs-c-promo-heading').text,
                'text': i.find('p', class_='gs-c-promo-summary').text, 
                'link': i.find('a', class_='gs-c-promo-heading')['href']
                }
        articles_json.append(article_obj)
    
    if output== 'text':
#        filename = 'C:\\Users\\lakeh\\Documents\\Python Scripts\\' + papername + str(date.today()) + '.txt'
#        with open(filename, 'w') as text_file:
#            print(articles, file=text_file) 
        return articles
    elif output == 'json':
        filename = 'C:\\Users\\lakeh\\Documents\\Python Scripts\\'+ papername + str(date.today()) + '.json'
        with open(filename, 'w') as outfile:
            json.dump(articles_json, outfile) 
        return articles_json
    else: print("""please set output = to 'json' or 'text'""")
    
def send_email(articles):
    gmail_user = 'chuckfinley1932@gmail.com'
    gmail_password = 'grnd9lake'
    
    sent_from = gmail_user
    to = ['lake.heckaman@ubs.com', 'lakeheckaman@gmail.com']
    subject = 'News ' + str(date.today())
    body = articles
    
    email_text = """\
    From: %s
    To: %s
    Subject: %s
    
    %s
    """ % (sent_from, ", ".join(to), subject, body)
    
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text.encode('utf8'))
        server.close()
    except:
        print('Something went wrong...')
        
news_scrapers = [scrape_SCMP, scrape_WSJ, scrape_BBC]
scrape_and_send(news_scrapers)