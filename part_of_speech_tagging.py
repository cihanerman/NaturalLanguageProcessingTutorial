#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:58:30 2019

@author: cihanerman
"""

import nltk as nl
#nl.download('averaged_perceptron_tagger') öğlerin listesi
text = "Anyone who reads Old and Middle English literary texts will be familiar with the mid-brown volumes of the EETS, with the symbol of Alfred's jewel embossed on the front cover. Most of the works attributed to King Alfred or to Aelfric, along with some of those by bishop Wulfstan and much anonymous prose and verse from the pre-Conquest period, are to be found within the Society's three series; all of the surviving medieval drama, most of the Middle English romances, much religious and secular prose and verse including the English works of John Gower, Thomas Hoccleve and most of Caxton's prints all find their place in the publications. Without EETS editions, study of medieval English texts would hardly be possible."
text = nl.word_tokenize(text)
text_oge = nl.pos_tag(text) # gramere dikkat edilmeyen yazılarda hatalı sonuç çıkarabilir.