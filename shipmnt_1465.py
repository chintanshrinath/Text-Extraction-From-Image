# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:38:19 2019

@author: Chintan
"""

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
        os.path.dirname(r"E:\Subject\udemy\shipmnts\OTH-M\1586"),
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

for i in range(1,11):
    hand=open('file'+str(i)+'.txt','rt')
    print("Details printing for",'file'+str(i)+'.txt')
    print("_________________________________________")

    for line in hand:
        line = line.rstrip()
        #Will find POW Number for file and print
        if re.search('^#\S', line):
            print("The POW NUMBER ",line)


    # *****************************************************
    #               Print Destination port
    # *****************************************************

    with open('file' + str(i) + '.txt', 'rt') as in_file:   
        searchstrings = ('BOM', 'BLR', 'HYD', 'CCU', 'MAA', 'DEL')
        for line in in_file:
            if any(word in line for word in searchstrings):
                
                c = line

    print('Destination Port ' + c)


