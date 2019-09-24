#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json

url="http://ufm.edu/Portal"
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
     
def portal():
    print("Alejandra Lemus")
    separator_parts()
    ##TITLE
    print ("GET the title and print it: "+soup.title.string)
    separator_items()
    
    ##ADDRESS
    address=soup.find("a", {"href": "#myModal"})   
    print("GET the Complete Address of UFM: "+address.text)
    separator_items()
    
    ##EMAIL AND PHONE NUMBER
    phone=soup.find("a", {"href": "tel:+50223387700"})
    email=soup.find("a", {"href": "mailto:inf@ufm.edu"})   
    print(f"GET the phone number: <{phone.text}> and info email: "+email.text)
    separator_items()
         
    ##UPPER NAV MENU   
    print("GET all item that are part of the upper nav menu (id: menu-table):")
    navmenu=soup.find_all("table", {"id": f"menu-table"})
    for items in navmenu:
        for navmenuitems in items.find_all("div"):
            menuitems=navmenuitems.string
            if menuitems is not None:
                    menuitems = str(menuitems).strip()
                    print(f"- {menuitems}")
       
    ##HREF             
    separator_items()
    print("find all properties that have href (link to somewhere):") 
    file = open("portal_find_all_properties_that_have_href.txt","w")
    print ("Output exceeds 30 lines, sending output to: <portal_find_all_properties_that_have_href.txt>")
    hrefs = []
    for refs in soup.find_all('a', href=True):
        hrefs.append(refs['href'])
        
    for item in hrefs:
        file.write("%s\n" % item)
    file.close()  
    
    ##UFMAIL
    separator_items()
    print("GET href of 'UFMail' button:")
    mailButton=soup.find(id="ufmail_")['href']
    print(f"{mailButton}")
    
    ##MIU
    separator_items()
    print("GET href 'MiU' button:")
    miuButton=soup.find(id="ufmail_")['href']
    print(f"{miuButton}")
    
    ##<IMG>
    separator_items()
    print("get hrefs of all <img>:")
    imgs=soup.find_all('img')
    for img in imgs:
        print (img['src'])

    ##<A>
    separator_items()
    count=0
    for a in soup.find_all("a"):
        count=count+1
    print("count all <a>: "+str(count))
 
def estudios():
    separator_parts()
    print("display all items from 'topmenu' (8 in total):")   
    separator_items
    print("display ALL 'Estudios':")
    separator_items
    print("display from 'leftbar' all <li> items:")
    separator_items
    print("get and display all available social media with its links:")
    separator_items
    print("count all <a>:")
    
def cs():
    separator_parts()
    
portal()