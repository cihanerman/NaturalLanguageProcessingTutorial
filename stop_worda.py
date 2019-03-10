#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:34:13 2019

@author: cihanerman
"""

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = 'Fazıl Say was born in 1970. He was a child prodigy, who was able to do basic arithmetic with 4-digit numbers at the age of two. His father, having found out that he was playing the melody of "Daha Dün Annemizin" on a makeshift flute with no prior training, enlisted the help of Ali Kemal Kaya, an oboe artist and a family friend. At the age of three, Say started his piano lessons under the tutelage of pianist Mithat Fenmen.'
text = word_tokenize(text)
text = [word for word in text if word not in stopwords.words('english')]