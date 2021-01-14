#Eric Gassel & Matthew Rasmussen 

import csv
import argparse

parser = argparse.ArgumentParser(description = 'Multiple ways to search through a csv file of authors and their books')
parser.add_argument('-a', '--authors', type = str, metavar='', help = 'prints a list of every author who contains given search string and prints a list of each author\'s books')

parser.add_argument('-t', '--titles', type = str, metavar='', help = 'prints a list of every book whose title contains given string')

parser.add_argument('-y', '--years', type = int, metavar='', help = 'prints a list of every book published between input year A and B, inclusive')

args = parser.parse_args()

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
        author= str(key) #jic key is not string 
        if authors.lower() in author.lower():
            print("-",author)
            keyList = author_dict[key]
            for i in range(len(author_dict[key])):
                print("    ", keyList[i])
            print("             ")
    return

def findTitles(titles): #titles command
    with open('books.csv') as csv_file:
        csv_reader= csv.reader(csv_file, delimiter=',')
        for row in csv_reader: 
            if titles.lower() in row[0].lower():
                print(row[0])
    return 

def findYears(year1, year2): #years command: also print our year with the book
    with open('books.csv') as csv_file:
        csv_reader= csv.reader(csv_file, delimiter=',')
        for row in csv_reader: 
            if int(row[1]) >= year1 and int(row[1]) <= year2:
                print(row[0], "-", row[1])
    return


if __name__ == "__main__":
    findAuthors(args.authors)
    #findTitles(args.titles)
    #findYears(args.year1, args.year2)

#def main():
    #print("hello")
    #authors("Jane")
    #authors("e")
    #titles("pride")
    #titles("the")
    #titles("and t")
    #years(1950, 1990)
#main()

