# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 22:17:46 2020

@author: john doe
"""
#### Operatiuni preliminare ####
from nltk.tokenize import word_tokenize, casual_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
# from nltk.stem import SnowballStemmer
# roStemmer=SnowballStemmer("romanian")
#### TASK 1 #### Tokenizer for corpus text #### Turbinca Tudor

corpusName = "corpus.txt"
corpusTagged = "corpus_tagged.txt"
def readCorpusFromFile(corpusName):
    file = open(corpusName,'r', encoding ="utf-8")
    return file.read()

def tokenizeText(text):
    return casual_tokenize(text)


text = readCorpusFromFile(corpusName)
listOfTokens = tokenizeText(text)
print(listOfTokens)
len(listOfTokens)
#### TASK 2 #### Lemmatization for corpus text ####

# def fileWords():
#     with open("word.txt","w+", encoding ="utf-8") as file1:
#         for tok in listOfTokens:
#             count_words = 0
#             for index in listOfTokens:
#                 if index == tok:
#                     count_words = count_words + 1
#             file1.write(str(tok) + ' ' + str(count_words) + '\n')
#         file1.close()
# fileWords()

# import nltk
# from nltk.stem import WordNetLemmatizer 
# wnl = WordNetLemmatizer()

# for words in listOfTokens :
#     print(words + "--->"+ roStemmer.stem(words))

# pip install rowordnet
# import rowordnet as rwn
### Lematizare Si WordPos #### 
import xml.etree.ElementTree as ET
lemmas = list()
pos_list = list()
tree = ET.parse('outputuri\corpus.xml')
root= tree.getroot()
for word in root.iter('W'):
    lemma = word.get('LEMMA')
    pos = word.get('POS')
    lemmas.append(lemma)
    pos_list.append(pos)


print(lemmas)
print(pos_list)

import pandas as pd
lg_p1= pd.DataFrame(list(zip(lemmas,pos_list)), columns=['lemmas', 'pos_list'])

text = open("corpus.txt", "r", encoding = "utf-8")
print(text)
d = dict()
for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
    for word in words:
        if word in words:
            if word in d:
                d[word] = d[word]+1
            else:
                d[word] = 1
#for key in list(d.keys()) :
#    print(key, ":", d)

from collections import Counter
numar = Counter(lemmas) 


