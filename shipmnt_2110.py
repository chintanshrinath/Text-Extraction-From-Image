# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 13:03:47 2019

@author: Chintan
"""

import io
import re
import os
from PIL import Image
from pytesseract import image_to_string

# =============================================================================
# text =image_to_string(Image.open('1.jpg'))
# text1 =image_to_string(Image.open('1.jpg'), lang='eng')
# 
# file=open(r"file_new1.txt","w+")
# file.writelines("hello world")
# file.close()
# =============================================================================

for i in range(1,11):
    file_name = os.path.join(
        os.path.dirname(r"E:\Subject\udemy\shipmnts\OTH-M\2110"),
        str(i)+'.jpg') # Your image path from current directory
    
    
   #open Image file and convert into text file
    with open(file_name, 'rb') as image_file:
        text1=image_to_string(Image.open(file_name))

    #write the text file
    for text in text1:
        with open('file'+str(i)+'.txt', 'a',encoding='utf-8') as f:
                f.write(text)

# =============================================================================
# Fetch Details for MAWB
# =============================================================================

for i in range(1, 10):
    pattern_occur = []  # The list where we will store results.
    pattern = re.compile(r"(\+\d{3})?[\s.-]?\d{3}[\s.-]?\d{4}[\s.-]?\d{4}") 
    try:  # Try to:
        with open('file' + str(i) + '.txt', 'rt') as in_file: 

            for linenum, line in enumerate(in_file):  
                if pattern.search(line) != None: 
                    pattern_occur.append(
                        (linenum, line.rstrip('\n')))  
                a = line
            print('\n\n')
            print('__________________________________')
            print('MAWB : ' + a)  

    except FileNotFoundError: 

        print("File Doesn't exist")  

    # *****************************************************
    #               Print Destination port
    # *****************************************************

    with open('file' + str(i) + '.txt', 'rt') as in_file:   
        searchstrings = ('BOM', 'BLR', 'HYD', 'CCU', 'MAA', 'DEL')
        for line in in_file:
            if any(word in line for word in searchstrings):
                
                c = line

    print('Destination Port ' + c[12:])


    # *****************************************************
    #               Weight
    # *****************************************************

    def get_weight(fp):
        next(line for line in fp if 'WEIGHT' in line or 'K' in line)
        for line in fp:
            try:
                return float(line)
            except ValueError:
                continue
        


    with open('file' + str(i) + '.txt', 'rt') as fd:
        print('Weight : ', get_weight(fd))


    # *****************************************************
    #               Cosignee
    # *****************************************************

    def get_address_line1(fp):
        next(line for line in fp if 'Jeena' in line)
        for line in fp:
            return line


    with open('file' + str(i) + '.txt', 'rt') as fd:
        print('Cosignee : JEENA & COMPANY, ', get_address_line1(fd))

