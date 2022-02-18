# -*- coding: utf-8 -*-
"""
@author: Sergio Leal
"""

def extract_and_count_letters(word):
    first_letter = word[0]
    last_letter = word[-1]
    letters_quantity = len(set(word[1:-1]))
    
    return first_letter,last_letter,letters_quantity