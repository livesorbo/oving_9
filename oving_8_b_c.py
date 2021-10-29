#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:31:55 2021

@author: livesorbo
"""

class FlervalgsSporsmal:
    def __init__(self, spm, ans, val):
        self.spm =spm
        self.ans=ans
        self.val=val
        
    def __str__(self):
        a=f"{self.spm}\n"
        for i in self.ans:
            a+= f"{self.ans.index(i)}:{i}\n"
        return a
    
    def skjekk_svar(self, bruker_svar):
       return bruker_svar== self.val
   
    def korrekt_svar_tekst(self):
        return f"Korrekt svar: {self.ans[self.val]}\n"
    
        
    
#spm1= FlervalgsSporsmal("Hvilken form har en ball?", ["firkant","rund", "trekant"], 2)
#print(spm1)
#svar= int(input("Svaret ditt:"))
#spm1.skjekk_svar(svar)

#spm2=FlervalgsSporsmal("Hvilken farge er sola?", ["gul", "grønn", "rosa"], 1)
#print(spm2)
#svar=int(input("Svaret ditt:"))
#spm2.skjekk_svar(svar)
