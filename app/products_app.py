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
    for i in range(1,len(all_products)):
        print('+' + str(all_products[i]))

def show():
    show_inp = input('Please specify the product\'s identifier: ')
    done = False
    for i in range(1,len(all_products)):
        if show_inp == all_products[i][0]:
            print(print(all_products[i]))
            done = True
            break
        else:
            continue
    if done != True:
        print('Please enter a valid identifier!')
        
def create():
    print('Please enter the following information:')
    name = input('Name: ')
    aisle = input('Aisle: ')
    dept = input('Department: ')
    price = input('Price: ')
    print('Creating product...')
    all_products.append([len(all_products), name, aisle, dept, price])
    print(all_products[len(all_products) - 1])

def update():
    update_inp = input('Please specify the product\'s identifier: ')
    found = False
    for i in range(1,len(all_products)):
        if update_inp == all_products[i][0]:
            found = True
            to_change = all_products[i]
            break
        else: 
            continue
    if found != True:
        print('Please enter a valid identifier!')
    else:
        print('Please enter the following information')
        name = input('Change name from %s to: ' %to_change[1])
        aisle = input('Change aisle from %s to: ' %to_change[2])
        dept = input('Change department from %s to: ' %to_change[3])
        price = input('Change price from %s to: ' %to_change[4])
        all_products[int(update_inp)] = [update_inp, name, aisle, dept, price]
        print('Creating a product!')
        print(str(all_products[int(update_inp)]))
    
def delete():
    del_inp = input('Please specify the product\'s identifier: ')
    found = False
    for i in range(1,len(all_products)):
        if del_inp == all_products[i][0]:
            found = True
            break
        else: 
            continue
    if found != True:
        print('Please enter a valid identifier!')
    else:
        print('Deleting product!')
        print(all_products.pop(int(del_inp)))

print('--------------------------\n\
Product Application\n--------------------------')
print('Welcome!')
print('There are %s products in the database. Please select an operation:\n\n\
List: Print a list of product identifiers and information.\n\
Show: Show information about a product.\n\
Create: Add a new product.\n\
Update: Edit an existing product.\n\
Delete: Delete an existing product.\n' %(len(all_products) - 1))

inp = input('Input command here: ')

input_handler(inp)

write_out(all_products)