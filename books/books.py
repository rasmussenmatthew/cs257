#Eric Gassel & Matthew Rasmussen 

import csv
import argparse

author_dict = {} 

#reading in csv file
with open('books.csv') as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',')
    #filling the dictionary to connect a list of books to each author
    for row in csv_reader:
        if row[2] not in author_dict: #no repeats
            author_dict[row[2]] = [row[0]]
        else:
            author_dict[row[2]].append(row[0])

    
def authors(name): #authors command
    for key in author_dict:
        author= str(key) #jic key is not string 
        if name.lower() in author.lower():
            print("-",author)
            keyList = author_dict[key]
            for i in range(len(author_dict[key])):
                print("    ", keyList[i])
            print("             ")
    return

def titles(name): #titles command
    with open('books.csv') as csv_file:
        csv_reader= csv.reader(csv_file, delimiter=',')
        for row in csv_reader: 
            if name.lower() in row[0].lower():
                print(row[0])
    return 

def years(year1, year2): #years command: also print our year with the book
    with open('books.csv') as csv_file:
        csv_reader= csv.reader(csv_file, delimiter=',')
        for row in csv_reader: 
            if int(row[1]) >= year1 and int(row[1]) <= year2:
                print(row[0], "-", row[1])
    return

def help1(): #print statement TBD
    return true


def main():
    print("hello")
    authors("Jane")
    #authors("e")
    titles("pride")
    #titles("the")
    #titles("and t")
    years(1950, 1990)
main()

