# -*- coding: utf-8 -*-
"""Assignment for internship webscraping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14i2PMKsBvCBelIoLwg5vXXyTbRD4Xa-H
"""

# Assignment 1 Web Scaraping
# Web scaraping project ideas quotes scrape

# What to scrape 
# 1. Name 
# 2. Quotes 
# 3. Tags

# Answer is divided into two parts 
# 1. In first part i have scraped the only first page 
# 2, In other part i have scraped the data of all the pages

"""Installing and Importing library required 

"""

!pip install bs4 
!pip install requests

from bs4 import BeautifulSoup
import requests
import pandas as pd

url="http://quotes.toscrape.com/page/1/"
site=requests.get(url)
site=site.content
soup=BeautifulSoup(site,"html.parser")
div=soup.find("div")
contents=div.find_all("div",class_="quote")



"""**Scraping the details of the first page**"""

details=[]
for content in contents:
  lines=content.find("span",class_="text").text
  author=content.find("small",class_="author").text
  tags = soup.find_all('div', class_='tags')
  tag_links = content.find_all('a')
  tag_names = [link.get_text() for link in tag_links][1:]
  details.append([lines,author,tag_names])

details[0]

data=pd.DataFrame(details,columns=["Quotes","Author","Tags used"])

data.head()

data.to_csv("scrapingdata.csv")



"""**Scraping the data for all the pages in the html in loop**"""

details=[]
for i in range(1,11):
  url=f"http://quotes.toscrape.com/page/{i}/"
  site=requests.get(url)
  site=site.content
  soup=BeautifulSoup(site,"html.parser")
  div=soup.find("div")
  contents=div.find_all("div",class_="quote")
  for content in contents:
    lines=content.find("span",class_="text").text
    author=content.find("small",class_="author").text
    tags = soup.find_all('div', class_='tags')
    tag_links = content.find_all('a')
    tag_names = [link.get_text() for link in tag_links][1:]
    details.append([lines,author,tag_names])



"""**Converting the list into dataframe**"""

scrapedata=pd.DataFrame(details,columns=["Quotes","Author","Tags Used"])

scrapedata.tail()



"""**Storing the dataframe into csv file**"""

scrapedata.to_csv("scapedata.csv")

