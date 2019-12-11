# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 01:33:10 2019

@author: Kartik
"""

import glob
import os
import re
from shutil import copy

# Viewing all the category names
diff_categories = []
pat = '^.*flat.*$' # Matching images with flat in their name

# Looping thru each product category in Raw Data
folders = glob.glob('./Data/Raw Data/*')
for folder in folders:
    diff_categories.append(folder.split('\\')[1])
    dest_train = './Data/Model Data/Train/'+folder.split('\\')[1]
    dest_valid = './Data/Model Data/Valid/'+folder.split('\\')[1]
    os.mkdir(dest_train) # Making destination folder for the train data
    os.mkdir(dest_valid) # Making destination folder for the validation data
    categories_contents = glob.glob(folder+'/*')
    count = 0
    
    # Looping thru each folder within category to count total usable images
    for category in categories_contents:
        folder_contents = glob.glob(category+'/*')
        for file in folder_contents:
            if re.search(pat, file)!= None:
                count+=1
    copied = 0
    
    # Copying 80% images in train and 20% in valid folders
    for category in categories_contents:
        folder_contents = glob.glob(category+'/*')
        for file in folder_contents:
            if re.search(pat, file)!= None:
                copied+=1
                if copied < int(count*4/5):
                    copy(file, dest_train+'/Train_Pic'+str(copied)+'.jpg')
                else:
                    copy(file, dest_valid+'/Valid_Pic'+str(copied)+'.jpg')