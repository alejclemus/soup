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
    
directorio()