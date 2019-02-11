# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 14:32:04 2019

@author: Chintan
"""
#Import libraries
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

for i in range(1,10):
    file_name = os.path.join(
        os.path.dirname(r"E:\Subject\udemy\shipmnts\OTH-M\OTH-M\80"),
        str(i)+'.jpg') # Your image path from current directory
    
    
   #open Image file and convert into text file
    with open(file_name, 'rb') as image_file:
        text1=image_to_string(Image.open(file_name))

    #write the text file
    for text in text1:
        with open('file'+str(i)+'.txt', 'a',encoding='utf-8') as f:
                f.write(text)


#starting print of  POW, PAF, Shipper etc
for i in range(1,10):
    hand=open('file'+str(i)+'.txt','rt')
    print("Details printing for",'file'+str(i)+'.txt')

    for line in hand:
        line = line.rstrip()
        #Will find POW Number for file and print
        if re.search('^POW-\S', line):
            print("The POW NUMBER ",line)
        #Will find PAF Number for file and print
        if re.search('PAF',line):
            print("The PAF number ", line)
        #Will find shipper name and print
        if re.search('Shipper:',line):
            print("The Shipper name " ,line)
        #Will find consignee name and rpint
        if re.search('Consignee:',line):
            print("The Consignee name ",line)
    print("==============================")

