# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:02:20 2017

@author: Mike
"""

import csv

prod = r'C:\Users\Mike\Documents\Current Courses\Python\crud\data\products.csv'

with open(prod, 'rb') as csvfile:
     reader = csv.reader(csvfile)