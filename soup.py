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

    
def portal():
    separator_parts()
    print ("GET the title and print it:")
    separator_items
    print("GET the Complete Address of UFM:")
    separator_items
    print("GET the phone number and info email:")
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
    print("display ALL 'Estudios'")
    separator_items
    print("display from 'leftbar' all <li> items")
    separator_items
    print("get and display all available social media with its links")
    separator_items
    print("count all <a>:")
    
def cs():
    separator_parts()
output = out_txt()
file = open("sample.txt","w")
file.write(output)
file.close()