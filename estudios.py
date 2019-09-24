#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json

url="http://ufm.edu/Estudios"

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
     
 
def estudios():
    separator_parts()  
    print("2. Estudios")
    ##ITEMS
    separator_items()
    print("display all items from 'topmenu':")
    topmenu=soup.find_all("div",{"id": f"topmenu"})     
    for items in topmenu:
        for menuitems in items.find_all("li"):
            topmenuitems=menuitems.string
            if topmenuitems is not None:
                topmenuitems=str(topmenuitems).strip()
                print(f"- {topmenuitems}")
                    
    ##ESTUDIOS
    separator_items()
    print("display ALL 'Estudios':")
    estudios=soup.find_all("div",{"class": "estudios"})
    for items in estudios:
        estudiositems=items.string
        if estudiositems is not None:
            estudiositems=str(estudiositems).strip()
            print(f"- {estudiositems}")
    
    ##LEFTBAR
    separator_items()
    print("display from 'leftbar' all <li> items:")
    leftbar=soup.find_all("div",{"class": f"leftbar"})
    for items in leftbar:
        for baritems in items.find_all("li"):
            leftbaritems=baritems.string
            if leftbaritems is not None:
                leftbaritems=str(leftbaritems).strip()
                print(f"- {leftbaritems}")
    
    ##SOCIAL MEDIA
    separator_items()
    print("get and display all available social media with its links:")
    socialmedia=soup.find('div',{"class": f"social pull-right"}).find_all("a")
    for links in socialmedia:
        print(f"- {links['href']}")
        
    ##<A>
    separator_items()
    count=0
    for a in soup.find_all("a"):
        count=count+1
    print("count all <a>: "+str(count))
    
    separator_parts()  
    
estudios()