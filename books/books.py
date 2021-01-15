#Eric Gassel & Matthew Rasmussen 

import csv
import argparse

#setting up parser and arguments 
parser = argparse.ArgumentParser(description = 'Multiple ways to search through a csv file of authors and their books')

parser.add_argument('-a', '--authors', type = str, metavar='', help = 'prints a list of every author who contains given search string and prints a list of each author\'s books')
parser.add_argument('-t', '--titles', type = str, metavar='', help = 'prints a list of every book whose title contains given string')
parser.add_argument('-y', '--years', nargs = 2, type = int, metavar='', help = 'prints a list of every book published between input year A and B, inclusive')

args = parser.parse_args()

#implementing new dictionary to be filled below 
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

    
def findAuthors(authors): #authors command
    for key in author_dict:
        author= str(key) #changing author (including lifespans) to string
        if authors.lower() in author.lower():
            print("-",author) #for spacing 
            keyList = author_dict[key]
            for i in range(len(author_dict[key])):
                print("    ", keyList[i])
            print("             ") #for spacing
    return

def findTitles(titles): #titles command
    with open('books.csv') as csv_file:
        csv_reader= csv.reader(csv_file, delimiter=',')
        for row in csv_reader: 
            if titles.lower() in row[0].lower():
                print(row[0])    
    print("             ") #for spacing 
    return 

def findYears(years): #years command: also prints out publish year of book
    if years[0] > years[1]: #ordering years so the smaller comes first
        yearsA = years[0]
        yearsB = years[1]
    else:                   
        yearsB = years[0]
        yearsA = years[1]
        
    with open('books.csv') as csv_file:
        csv_reader= csv.reader(csv_file, delimiter=',')
        for row in csv_reader: 
            if int(row[1]) >= yearsB and int(row[1]) <= yearsA:
                print(row[0], "-", row[1])
    print("             ") #for spacing 
    return

def main():
    #if statments to see which function is being used
    if args.authors != None:
        findAuthors(args.authors)
    if args.titles != None:
        findTitles(args.titles)
    if args.years != None:
        findYears(args.years)

if __name__ == "__main__":
    main()



