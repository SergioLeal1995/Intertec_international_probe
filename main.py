# -*- coding: utf-8 -*-
"""
@author: Sergio Leal
"""

import re
from extract_function import extract_and_count_letters

sentenceParser = 'Creativity is thinking-up new things. Innovation is doing new things!'
#sentenceParser = 'Smooth'
words = sentenceParser.split()

def wordParser(words):
    output = []
    for word in words:
        if len(word)>2:
            if not word.isalnum(): 
               
                symbol = []
                patron = re.compile(r"[^a-zA-Z0-9]") 
                word_pieces = patron.split(word)     
                word_lenght = len(word_pieces[0])    
                symbol.append(word[word_lenght])     
                first_letter,last_letter,letters_quantity = extract_and_count_letters(word_pieces[0])
                output.append(first_letter + str(letters_quantity) + last_letter + symbol[0] + word_pieces[-1])
            
            else:
                first_letter,last_letter,letters_quantity = extract_and_count_letters(word)
                output.append(first_letter + str(letters_quantity) + last_letter)
            
        else:
            output.append(word)
    out = " ".join(output)        
    return out

if __name__ == "__main__":
   print(wordParser(words))