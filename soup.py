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
    print ("GET the title and print it:")
    print("GET the Complete Address of UFM:")
    print("GET the phone number and info email:")
    print("GET all item that are part of the upper nav menu (id: menu-table):")
    print("find all properties that have href (link to somewhere):")
    print("GET href of 'UFMail' button:")
    print("GET href 'MiU' button:")
    print("get hrefs of all <img>")
    print("count all <a>:")
    
output = out_txt()
file = open("sample.txt","w")
file.write(output)
file.close()