#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:08:17 2019

@author: cihanerman
"""

from nltk.tokenize import sent_tokenize, word_tokenize

text = 'Alan Mathison Turing, İngiliz matematikçi, bilgisayar bilimcisi ve kriptolog. Bilgisayar biliminin kurucusu sayılır. Geliştirmiş oldugu Turing testi ile makinelerin ve bilgisayarların düşünme yetisine sahip olup olamayacakları konusunda bir kriter öne sürmüştür.'
#text = text.split()
text1 = word_tokenize(text)
text2 = sent_tokenize(text)