# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 07:56:31 2020

@author: john doe
"""
import bs4
from bs4 import BeautifulSoup
import requests
import csv

url = requests.get('https://www.patriabank.ro/blog/resurse/impactul-crizei-covid19-mediu-de-afaceri-romania').text

soup = BeautifulSoup(url, 'html.parser')

#csv_file = open('articole.csv', 'w',  encoding ='utf-16')
#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(['Titlu', 'Articol'])
print(soup.prettify())

titlu = soup.find('h1').text

print(titlu)

articolul = soup.find('div', class_='content').text

print(articolul)

#csv_writer.writerow([titlu, articolul]) 
#csv_file.close()
#csv.field_size_limit()

with open('articole.csv', 'w',newline='', encoding="utf-16") as csvfile:
    fieldnames = ['Titlu', 'Articol']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames, delimiter = '\t')
    writer.writeheader()
    writer.writerow({"Titlu": titlu.replace("\n", " ").strip(), "Articol": articolul.replace("\n", " ").strip()})
