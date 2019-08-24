# -*- coding: utf-8 -*-

import smtplib
from datetime import date


def send_email(articles, credentials, recipients):
    #load text file with email address and password - to keep offline for security 
    with open(credentials, mode='r') as file:
        content = file.read().split('\n')
     #use contents of text file to set user and password vars  
    gmail_user = content[0]
    gmail_password = content[1]
    
    sent_from = gmail_user
    to = recipients
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