#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 11:43:45 2021

@author: livesorbo
"""

from oving_9_d import  spm

if __name__ == "__main__":
    spiller_1_teller=0
    spiller_2_teller=0
    
    for spors in spm():
        print(spors)
        svar_spiller_1=int(input("Skriv inn svar for spiller 1: "))
        svar_spiller_2=int(input("Skriv inn svar for spiller 2: "))
        
        print(f"\n{spors.korrekt_svar_tekst()}")
        
        if spors.skjekk_svar(svar_spiller_1) == True:
            print("Spiller 1: Korrekt svar \n")
            spiller_1_teller += 1
        else:
            print("Spiller 1: Feil\n")
        if spors.skjekk_svar(svar_spiller_2) == True:
            print("Spiller 2: Korrekt svar")
            spiller_2_teller+=1
        else:
            print("Spiller 2: Feil \n")
    
    print(f"Spiller 1 fikk {spiller_1_teller} korrekte svar")
    print(f"Spiller 2 fikk {spiller_2_teller} korrekte svar")
    