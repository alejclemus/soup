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

def out_txt():
    print ("Output exceeds 30 lines, sending output to: <logfile>")
    return "Hello World"

def easyprint (element,name):
  for each_div in soup.findAll(element,{'class':name}):
      print (each_div)
          
def portal():
    separator_parts()
    print ("GET the title and print it: "+soup.title.string)
    separator_items
    address=soup.find("a", {"href": "#myModal"})   
    print("GET the Complete Address of UFM: "+address.text)
    separator_items
    phone=soup.find("a", {"href": "tel:+50223387700"})
    email=soup.find("a", {"href": "mailto:inf@ufm.edu"})   
    print("GET the phone number and info email:"+phone+email)
    separator_items
    print("GET all item that are part of the upper nav menu (id: menu-table):")
    separator_items
    print("find all properties that have href (link to somewhere):")
    separator_items
    print("GET href of 'UFMail' button:")
    separator_items
    print("GET href 'MiU' button:")
    separator_items
    print("get hrefs of all <img>")
    separator_items
    print("count all <a>:")
 
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
    
output = out_txt()
file = open("sample.txt","w")
file.write(output)
file.close()

portal()