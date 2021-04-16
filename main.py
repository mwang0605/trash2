
import os
# Import requests (to download the page)
import requests

import random
# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

import nltk
# Import smtplib (to allow us to email)
import smtplib

server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.ehlo()
server.starttls()
server.login('mwang0605@gmail.com', 'Mw06052008')

# This is a pretty simple script. The script downloads the homepage of VentureBeat, and if it finds some text, emails me.
# If it does not find some text, it waits 60 seconds and downloads the homepage again.
# set the url as VentureBeat,
url = "https://www.centurycommunities.com/find-your-home/georgia/dalton-metro/jefferson/oconee-station"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# download the homepage
import datetime

# parse the downloaded homepage and grab all text, then,

# while this is true (it is true by default),

response = requests.get(url, headers=headers)

html = response.text

soup = BeautifulSoup(html, "html5lib")

text = soup.get_text(strip=True)

random_int = random.randint(0, 9)

audit_log = []

while True:
    print(str(soup).find("Buy Now"))
    if str(soup).find("Buy Now") == -1:
        print("Buy Now Wasn't Found")
        now = datetime.datetime.now()
        audit_log.append(str(now))
        print("website checked @ " + str(audit_log))

        # wait 60 seconds,
        time.sleep(20 + random_int)
        # continue with the script,

    # but if the word "Google" occurs any other number of times,
    else:
        print('changes')
        file = "anoying.mp3"
        os.system(file)
        os.system(file)
        os.system(file)
        subject = 'CHANGE DETECTED'
        body = 'THERE WAS A CHANGE DETECTED @ ' + url + "BUY NOW WAS FOUND!!! POTENTIAL RELEASE"
        message = f'Subject: {subject}\n\n{body}'
        # server.sendmail('mwang0605@gmail.com', 'mjlts2017@gmail.com',message)
        server.sendmail('mwang0605@gmail.com', 'mwang0605@gmail.com', message)
        server.quit()

        break



