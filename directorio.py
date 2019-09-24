#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json

url="https://www.ufm.edu/Directorio"

# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

# print if needed, gets too noisy
#print(soup.prettify())

def separator_items():
    print ("-----------------------------------------------------------------------------------------------------------------------------")
    
def separator_parts():
    print ("=============================================================================================================================")

def directorio():
    separator_parts()
    
    ##EMAILS
    print("Sort all emails alphabetically (href='mailto:arquitectura@ufm.edu') in a list, dump it to logs/4directorio_emails.txt")
    file = open("logs/4directorio_emails.txt","w")
    mails=[]
    for datamails in soup.find_all(attrs={"href":True}):
            if str(datamails['href']).__contains__("mailto"):
                mails.append(str(datamails['href'].replace("mailto:","")))
    
    mails.sort()
    mails=list(dict.fromkeys(mails))
    for item in mails:
        file.write("%s\n" % item)
    file.close()  
    
    ##ALPHABET
    words = mails
    words_starting_with_vowel = [word for word in words if word[0] in 'aeiou']
    count=0
    for a in words_starting_with_vowel:
        count=count+1
    print("Count all emails that start with a vowel: "+str(count))

directorio()