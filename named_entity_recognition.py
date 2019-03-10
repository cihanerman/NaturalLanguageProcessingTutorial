#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:05:39 2019

@author: cihanerman
"""
# metinlerden kişi, yer, tarih bilgilerini çıkarmaya yarıyor.
import nltk as nl
#nl.download('maxent_ne_chunker')
#nl.download('words')

text = "Atatürk came to prominence for his role in securing the Ottoman Turkish victory at the Battle of Gallipoli (1915) during World War I. Following the Empire's defeat and subsequent dissolution, he led the Turkish National Movement, which resisted the mainland Turkey's partition among the victorious Allied powers. Establishing a provisional government in the present-day Turkish capital Ankara, he defeated the forces sent by the Allies, thus emerging victorious from what was later referred to as the Turkish War of Independence. He subsequently proceeded to abolish the decrepit Ottoman Empire and proclaimed the foundation of the Turkish Republic in its place."
tokenized = nl.word_tokenize(text)
tagged = nl.pos_tag(tokenized)
named_en = nl.ne_chunk(tagged)
named_en.draw()