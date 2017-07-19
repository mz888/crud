# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:02:20 2017

@author: Mike
"""

import csv

path = r'C:\Users\Mike\Documents\Current Courses\Python\crud\data'

all_products = []

with open(path + '\products.csv', 'r') as csvfile:
    products = csv.reader(csvfile)
    for row in products:
        all_products.append(row)

# function for writing output to csv
def write_out(out_products):
    with open(path + '\products.csv', 'w') as out:
        writer = csv.writer(out, lineterminator = '\n')
        for each in out_products:
            writer.writerow(each)

# input handler
def input_handler(inp):
    if inp == 'List':
        printlist()
    elif inp == 'Show':
        show()
    elif inp == 'Create':
        create()
    elif inp == 'Update':
        update()
    elif inp == 'Delete':
        delete()
    else:
        print('Unrecognized command: please enter one of the following: List, Show, Create, Update, or Delete')

def printlist():
    print('There are %s products:' %(len(all_products) - 1))
    

print('--------------------------\n\
Product Application\n--------------------------')

print('There are %s products in the database. Please select an operation:\n\n\
List: Print a list of product identifiers and information.\n\
Show: Show information about a product.\n\
Create: Add a new product.\n\
Update: Edit an existing product.\n\
Delete: Delete an existing product.\n' %(len(all_products) - 1))

inp = input('Input command here: ')

input_handler(inp)

