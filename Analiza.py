# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 12:00:44 2021

@author: john doe
"""
#pip install polyglot

import pandas as pd 
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt  
from sklearn import datasets, metrics, model_selection, svm
import numpy as np

#from textblob import TextBlob
#pip install wordcloud
#from wordcloud import WordCloud
#import re
#def getPolarity(text) :
#    return TextBlob(text).sentiment.polarity
#articole['polarity'] = articole['Articol'].apply(getPolarity)
#articole
    
#pip install -U textblob
#from textblob import TextBlob
#from textblob.sentiments import NaiveBayesAnalyzer
#blob1 = TextBlob("Performanţa economică se va reduce în acest an marcat de pandemia de coronavirus în întreaga lume, avertizează la unison specialiştii. Nu există niciun indiciu care să ateste altceva. Controverse se poartă doar legat de dimensiunea reculului economic şi de şansele de calmare a situaţiei pe termen mediu.", analyzer= NaiveBayesAnalyzer())
#blob1.sentiment
#pip install polyglot==14.11
#import polyglot
#from polyglot.downloader import downloader
#print(downloader.supported_languages_table("sentiment2", 3))

articole = pd.read_excel('articole_analiza.xlsx')
articole = pd.DataFrame(articole)
type(articole)
articole.head()

####  TFIDF vectorizer

stopset = set(stopwords.words('romanian'))
vectorizer = TfidfVectorizer(use_idf= True, lowercase=True, strip_accents='ascii', stop_words=stopset)

#### Declararea variabilei dependente

y= articole.Categorie

#### Convertirea articole111.xlsx 

X = vectorizer.fit_transform(articole.Articol)                             
####
print (y.shape)
print (X.shape)

#### Test train split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

#### Naive bayes classifer :
clf = naive_bayes.MultinomialNB()
clf.fit(X_train, y_train)

### Acurracy

roc_auc_score(y_test, clf.predict_proba(X_test)[:,1])

###Grafic
metrics.plot_roc_curve(clf, X_test, y_test)  
plt.show()   
#### Test ###

new_art_array= np.array(["Performanţa economică se va reduce în acest an marcat de pandemia de coronavirus în întreaga lume, avertizează la unison specialiştii. Nu există niciun indiciu care să ateste altceva. Controverse se poartă doar legat de dimensiunea reculului economic şi de şansele de calmare a situaţiei pe termen mediu."])
new_art_vector = vectorizer.transform(new_art_array)
print (clf.predict(new_art_vector))
