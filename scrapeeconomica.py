# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:47:21 2020

@author: john doe
"""
import bs4
from bs4 import BeautifulSoup
import requests
import csv
import re
url = requests.get('https://www.economica.net/thomas-schiefer-director-general-zirom-romania_192115.html').text

soup = BeautifulSoup(url, 'html.parser')

#csv_file = open('articole.csv', 'w',  encoding ='utf-16')
#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(['Titlu', 'Articol'])
print(soup.prettify())

titlu = soup.find('h1', class_='mb-5 font-weight-bold').text

print(titlu)

articol = soup.find('div', class_='col-12 article-content')
articolul =""
for hit in articol.findAll('p'):
        hit = hit.text.strip()
        articolul = articolul + hit
        print(hit)
print(articolul)
#csv_writer.writerow([titlu, articolul])
#csv_file.close()
#csv.field_size_limit()

with open('articole.csv', 'a', newline='', encoding="utf-16") as csvfile:
    fieldnames = ['Titlu', 'Articol']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames, delimiter = '\t')
    writer.writerow({"Titlu": titlu.replace("\n", " ").strip(), "Articol": articolul.replace("\n", " ").strip()})