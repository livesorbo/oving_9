#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:55:53 2021

@author: livesorbo
"""

from oving_8_b_c import FlervalgsSporsmal

def spm():
    liste=[]
    with open ("sporsmaalsfil.txt", "r", encoding="UTF8") as spmfil:
        for linje in spmfil:
            linje=linje.strip().split(":")
            
            alt_liste=linje[2].split(",")
            for i in range(len(alt_liste)):
                alt_liste[i]=alt_liste[i].strip("[ ]")
                
            liste.append(FlervalgsSporsmal(linje[0], alt_liste, int(linje[1])))
        return liste
    
            
        
        