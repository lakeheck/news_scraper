# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 14:05:40 2019

@author: lakeh
"""

                                
from selenium import webdriver                           

def wsj_login():
    driver = webdriver.Chrome('C:\\Users\\lakeh\\Programs\\chromedriver.exe')
    driver.get('https://sso.accounts.dowjones.com/login?state=g6Fo2SBxeHIyVllHUmdEMEZGZ210dGRnX1JSdXUxUWlkdXBpZqN0aWTZIHoxNFhWaHRDVnV5U3VMMWQtaTNERFBTZXZ3cHdvcTNQo2NpZNkgNWhzc0VBZE15MG1KVElDbkpOdkM5VFhFdzNWYTdqZk8&client=5hssEAdMy0mJTICnJNvC9TXEw3Va7jfO&protocol=oauth2&scope=openid%20idp_id%20roles%20email%20given_name%20family_name%20djid%20djUsername%20djStatus%20trackid%20tags%20prts&response_type=code&redirect_uri=https%3A%2F%2Faccounts.wsj.com%2Fauth%2Fsso%2Flogin&nonce=ece006c1-9f3f-4104-8e46-17d05dd88dea&connection=DJldap&ui_locales=en-us-x-wsj-19-2&ns=prod%2Faccounts-wsj&savelogin=on#!/signin')
    
    u = driver.find_element_by_id("username")
    
    p = driver.find_element_by_id("password")
    
    u.send_keys("gdai1@nd.edu")
    
    p.send_keys("Intern2018!")
    
    login_attempt = driver.find_element_by_class_name("sign-in")
    login_attempt.submit()
