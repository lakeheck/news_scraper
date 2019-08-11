# -*- coding: utf-8 -*-

import smtplib
from datetime import date


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