#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json

url="https://fce.ufm.edu/carrera/cs/"

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
     
def cs():
    separator_parts()
    print("3. CS")
    ##TITLE
    print("GET title: "+soup.title.string)
    
    ##LOGO
    separator_items()
    print("Download the 'FACULTAD de CIENCIAS ECONOMICAS' logo. (you need to obtain the link dynamically)")
    
    
    ##META
    separator_items()
    print(f"GET following <meta>: 'title', 'description' ('og')")
    title = soup.find("meta",  property="og:title")
    description = soup.find("meta",  property="og:description")
    print(f"- title: {title['content']}")
    print(f"- description: {description['content']}")
    
    ##<a>
    separator_items()
    countA=0
    for a in soup.find_all("a"):
        countA=countA+1
    print("count all <a>: "+str(countA))
    
    ##<div>
    separator_items()
    countD=0
    for div in soup.find_all("div"):
        countD=countD+1
    print("count all <div>: "+str(countD))
    
    separator_parts()
    
cs()
