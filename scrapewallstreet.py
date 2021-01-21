# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:50:58 2020

@author: john doe
"""
import bs4
from bs4 import BeautifulSoup
import requests
import csv

url = requests.get('https://www.wall-street.ro/articol/International/265036/in-ultimele-zile-de-mandat-trump-pune-pe-masa-un-plan-de-relansare-a-economiei-americane-de-916-mld-dolari.html').text

soup = BeautifulSoup(url, 'html.parser')

#csv_file = open('articole.csv', 'w',  encoding ='utf-16')
#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(['Titlu', 'Articol'])
print(soup.prettify())

titlu = soup.find('h1').text

print(titlu)

articol = soup.find('div', class_='articleText')
articolul =""
for hit in articol.findAll('p'):
        hit = hit.text.strip()
        articolul = articolul + hit
        print(hit)
print(articolul)

#csv_writer.writerow([titlu, articolul])
#csv_file.close()
#csv.field_size_limit()

with open('articole1.csv', 'a',newline='', encoding="utf-16") as csvfile:
    fieldnames = ['Titlu', 'Articol']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames, delimiter = '\t')
    writer.writerow({"Titlu": titlu.replace("\n", " ").strip(), "Articol": articolul.replace("\n", " ").strip()})