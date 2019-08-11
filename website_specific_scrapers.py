# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 16:02:33 2019

@author: lakeh
"""
import requests
from bs4 import BeautifulSoup
from datetime import date
import json
from nlp_methods import generate_summary
import lxml
from logins import *

def scrape_SCMP(output='text'):
    #select url   
    papername = "SCMP"
    url = 'https://www.scmp.com/news'
    #pull data from API
    r1=requests.get(url)
    coverpage = r1.content
    #convert to soup
    soup = BeautifulSoup(coverpage, features="lxml")
    #find the first main article section and then pull all articles that have summaries from this section
    t = soup.find('div', class_="main-article-section-content").find_all('div', class_='article__summary')
    #pull the link, title, summary text from these articles   
    articles=str()
    articles_json = []
    for i in t:
        #link = i.parent.find('div', class_='article__title').find('a')['href']
        title = i.parent.find('div', class_='article__title').text
        text = i.text
        link = f"https://www.scmp.com{i.parent.find('div', class_='article__title').find('a')['href']}"

       # now we extract the full text from each article and summarize it 
#        text = str()
#        r2=requests.get(link)
#        coverpage = r2.content
#        soup = BeautifulSoup(coverpage, features="lxml")
#        #find the first main article section and then pull all articles that have summaries from this section
#        for pp in soup.find_all('p', class_='article__body'):
#            text += pp.text
#        summary = generate_summary(text,summary_lines)
        #concat it all together
        string = (
                f"{title}.\n"
                f"{text}\n"
                f"{link}\n\n\n"
                )
        if string in articles: pass
        else: articles += string
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
      
def scrape_WSJ(output = 'text', summary_lines=3):
    driver = webdriver.Chrome('C:\\Users\\lakeh\\Programs\\chromedriver.exe')
    driver.get('https://sso.accounts.dowjones.com/login?state=g6Fo2SBxeHIyVllHUmdEMEZGZ210dGRnX1JSdXUxUWlkdXBpZqN0aWTZIHoxNFhWaHRDVnV5U3VMMWQtaTNERFBTZXZ3cHdvcTNQo2NpZNkgNWhzc0VBZE15MG1KVElDbkpOdkM5VFhFdzNWYTdqZk8&client=5hssEAdMy0mJTICnJNvC9TXEw3Va7jfO&protocol=oauth2&scope=openid%20idp_id%20roles%20email%20given_name%20family_name%20djid%20djUsername%20djStatus%20trackid%20tags%20prts&response_type=code&redirect_uri=https%3A%2F%2Faccounts.wsj.com%2Fauth%2Fsso%2Flogin&nonce=ece006c1-9f3f-4104-8e46-17d05dd88dea&connection=DJldap&ui_locales=en-us-x-wsj-19-2&ns=prod%2Faccounts-wsj&savelogin=on#!/signin')
    
    u = driver.find_element_by_id("username")
    
    p = driver.find_element_by_id("password")
    
    u.send_keys("gdai1@nd.edu")
    
    p.send_keys("Intern2018!")
    
    login_attempt = driver.find_element_by_class_name("sign-in")
    login_attempt.submit()
    #select url   
    papername = "WSJ"
    url = 'https://www.wsj.com/news/markets'
    #pull data from API
    r1=requests.get(url)
    coverpage = r1.content
    #convert to soup
    soup = BeautifulSoup(coverpage, features="lxml")     
               
    #find the first main article section and then pull all articles that have summaries from this section
    t = soup.find('div', class_="lead-story").find_all('h3', class_='wsj-headline')
    #pull the link, title, summary text from these articles   
    articles=str()
    count = 0
    articles_json = []
    for i in t:
        try: 
            count += 1
#            link = i.find('a', class_='wsj-headline-link')['href']
            summary = i.parent.find('p', class_='wsj-summary').text
            title = i.text
            link = f"{i.find('a', class_='wsj-headline-link')['href']}"

            #now we extract the full text from each article and summarize it 
            try:
                text = str()
                r2=requests.get(link)
                coverpage = r2.content
                soup = BeautifulSoup(coverpage, features="lxml")
                #find the first main article section and then pull all articles that have summaries from this section
                for pp in soup.find_all('p', attrs={'class': None}):
                    text += pp.text
                summary = generate_summary(text,summary_lines)
            except: pass
            #concat it all together
            string = (
                    f"{title}.\n"
                    f"{text}\n"
                    f"{link}\n\n\n"
                    )
            if string in articles: pass
            else: articles += string
            article_obj = {
                'title': title, 
                'text': text, 
                'link': link
                }
            articles_json.append(article_obj)
        except:"Nonetype"
    driver.quit()
    #write articles to a file and return, depending on output type specified
    if output== 'text':
        filename = 'C:\\Users\\lakeh\\Documents\\Python Scripts\\' + papername + str(date.today()) + '.txt'
        with open(filename, 'w') as text_file:
            print(articles, file=text_file) 
        return articles
    elif output == 'json':
        filename = 'C:\\Users\\lakeh\\Documents\\Python Scripts\\'+ papername + str(date.today()) + '.json'
        with open(filename, 'w') as outfile:
            json.dump(articles_json, outfile) 
        return articles_json
    else: print("""please set output = to 'json' or 'text'""")

def scrape_BBC(output = 'text', summary_lines=3):
    #select url   
    papername = "BBC"  
    url = 'https://www.bbc.com/news'
    #pull data from API
    r1=requests.get(url)
    coverpage = r1.content
    #convert to soup
    soup = BeautifulSoup(coverpage, features="lxml")     
               
    #find the first main article section and then pull all articles that have summaries from this section
    t = soup.find('div', class_="nw-c-top-stories--standard").find_all('div', class_='gs-c-promo-body')
    #pull the link, title, summary text from these articles and store in dict to convert to json
    articles=str()
    articles_json = []
    for i in t:
        link = f"https://www.bbc.com{i.find('a', class_='gs-c-promo-heading')['href']}"
#        link = i.find('a', class_='gs-c-promo-heading')['href']
        summary = i.find('p', class_='gs-c-promo-summary').text
        title = i.find('a', class_='gs-c-promo-heading').text
        #now we extract the full text from each article and summarize it 
        try: 
            text = str()
            r2=requests.get(link)
            coverpage = r2.content
            soup = BeautifulSoup(coverpage, features="lxml")
            #find the first main article section and then pull all articles that have summaries from this section
            for pp in soup.find_all('p', attrs={'class': None}):
                text += pp.text
            summary = generate_summary(text,summary_lines)
        except: pass
        #concat it all together
        string = (
                f"{title}.\n"
                f"{summary}\n"
                f"{link}\n\n\n"
                )
        if string in articles: pass
        else: articles += string
        #store into dict for json
        article_obj = {
                'title': i.find('a', class_='gs-c-promo-heading').text,
                'text': i.find('p', class_='gs-c-promo-summary').text, 
                'link': i.find('a', class_='gs-c-promo-heading')['href']
                }
        articles_json.append(article_obj)
    
    if output== 'text':
        filename = 'C:\\Users\\lakeh\\Documents\\Python Scripts\\' + papername + str(date.today()) + '.txt'
        with open(filename, 'w') as text_file:
            print(articles, file=text_file) 
        return articles
    elif output == 'json':
        filename = 'C:\\Users\\lakeh\\Documents\\Python Scripts\\'+ papername + str(date.today()) + '.json'
        with open(filename, 'w') as outfile:
            json.dump(articles_json, outfile) 
        return articles_json
    else: print("""please set output = to 'json' or 'text'""")


def scrape_AlJazeera(output='text', summary_lines=3):
    #select url   
    papername = "Al Jazeera"
    url = 'https://www.aljazeera.com/news/'
    #pull data from API
    r1=requests.get(url)
    coverpage = r1.content
    #convert to soup
    soup = BeautifulSoup(coverpage, features="lxml")
    #find the first main article section and then pull all articles that have summaries from this section
    t = soup.find('div', class_="top-topics-wrapper").find_all('h2', class_=['top-sec-title', 'top-sec-smalltitle'])
    #pull the link, title, summary text from these articles   
    articles=str()
    articles_json = []
    for i in t:
        link = f"https://www.aljazeera.com{i.parent['href']}"
        title = i.text
        try: 
            summary = i.parent.next_sibling.text
        except:
            summary = str()
        #use beautiful soup agian to access main text of article and summarize it
        try: 
            text = str()
            r2=requests.get(link)
            coverpage = r2.content
            soup = BeautifulSoup(coverpage, features="lxml")
            #find the first main article section and then pull all articles that have summaries from this section
            for pp in soup.find_all('p'):
                text += pp.text
            summary = generate_summary(text,summary_lines)
        except: pass

        #concat it all together
        string = (
                f"{title}.\n"
                f"{summary}\n"
                f"{link}\n\n\n"
                )
        if string in articles: pass
        else: articles += string
        article_obj = {
            'title': title, 
            'text': text, 
            'link': link
            }
        articles_json.append(article_obj)
    #write articles to a file and return, depending on output type specified
    if output== 'text':
#        filename = 'C:\\Users\\lakeh\\Documents\\Python Scripts\\' + papername + str(date.today()) + '.txt'
#        with open(filename, 'w', encoding='utf8') as text_file:
#            print(articles, file=text_file) 
        return articles
    elif output == 'json':
        filename = 'C:\\Users\\lakeh\\Documents\\Python Scripts\\'+ papername + str(date.today()) + '.json'
        with open(filename, 'w') as outfile:
            json.dump(articles_json, outfile) 
        return articles_json
    else: print("""please set output = to 'json' or 'text'""")
    

