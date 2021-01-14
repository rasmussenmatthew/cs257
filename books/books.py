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
                print("   ", keyList[i])
    return

def titles(name): #titles command
    #idea: still use the dictionary, look through each key's list and if title matches, then print title with author's name
        #ex: --title pride and 
            #-Pride and Prejudice by Jane Austin
    #could also not include title but I thought we'd make decent use of dictionary
    return true

def years(year1, year2): #years command: also print our year with the book
    return true

def help1(): #print statement TBD
    return true


def main():
    print("hello")
    authors("Jane")
main()

