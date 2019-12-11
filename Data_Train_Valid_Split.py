# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 01:33:10 2019

@author: Kartik
"""

import glob
import os
import re
from shutil import copy

diff_categories = []
pat = '^.*flat.*$'

os.chdir(r'C:\Users\Kartik\Desktop\Study Material\E-commerce Tech\Project\Neuro-pic\Categorizing Project\Iterations\Denim_Sweaters Project')

folders = glob.glob('./Data/Raw Data/*')
for folder in folders:
    diff_categories.append(folder.split('\\')[1])
    dest_train = './Data/Model Data/Train/'+folder.split('\\')[1]
    dest_test = './Data/Model Data/Test/'+folder.split('\\')[1]
    os.mkdir(dest_train)
    os.mkdir(dest_test)
    categories_contents = glob.glob(folder+'/*')
    count = 0
    for category in categories_contents:
        folder_contents = glob.glob(category+'/*')
        for file in folder_contents:
            if re.search(pat, file)!= None:
                count+=1
    copied = 0
    for category in categories_contents:
        folder_contents = glob.glob(category+'/*')
        for file in folder_contents:
            if re.search(pat, file)!= None:
                copied+=1
                if copied < int(count*4/5):
                    copy(file, dest_train+'/Train_Pic'+str(copied)+'.jpg')
                else:
                    copy(file, dest_test+'/Test_Pic'+str(copied)+'.jpg')
