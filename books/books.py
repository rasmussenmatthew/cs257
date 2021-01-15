#Eric Gassel & Matthew Rasmussen 

import csv
import argparse

#setting up parser and arguments 
parser = argparse.ArgumentParser(description = 'Multiple ways to search through a csv file of authors and their books')

parser.add_argument('-a', '--authors', type = str, metavar='', help = 'prints a list of every author who contains given search string and prints a list of each author\'s books')
parser.add_argument('-t', '--titles', type = str, metavar='', help = 'prints a list of every book whose title contains given string')
parser.add_argument('-y', '--years', nargs = 2, type = int, metavar='', help = 'prints a list of every book published between input year A and B, inclusive')

args = parser.parse_args()

    
def findAuthors(authors): #authors command
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
                
    counter = 0        
    for key in author_dict: #looping through dictionary
        author= str(key) #changing author (including lifespans) to string
        if authors.lower() in author.lower():
            counter += 1
            print("-",author) #for spacing 
            keyList = author_dict[key]
            for i in range(len(author_dict[key])):
                print("    ", keyList[i])
            print("             ") #for spacing
    if counter == 0:
        print("There is no author whose name conatins the given string")
        print("             ") #for spacing
    return

def findTitles(titles): #titles command
    counter = 0 
    with open('books.csv') as csv_file:
        csv_reader= csv.reader(csv_file, delimiter=',')
        for row in csv_reader: 
            if titles.lower() in row[0].lower():
                counter += 1
                print(row[0], "written by", row[2], "in", row[1])    
                print("             ") #for spacing 
                
    if counter == 0: #message to user if no books are found
        print("There is no book whose title contains the given string.")
    print("             ") #for spacing 
    return 

def findYears(years): #years command: also prints out publish year of book
    if years[0] > years[1]: #ordering years so the smaller comes first
        yearsA = years[0]
        yearsB = years[1]
    else:                   
        yearsB = years[0]
        yearsA = years[1]
        
    counter = 0 
    with open('books.csv') as csv_file:
        csv_reader= csv.reader(csv_file, delimiter=',')
        for row in csv_reader: 
            if int(row[1]) >= yearsB and int(row[1]) <= yearsA:
                counter += 1
                print(row[0], "written by", row[2], "in", row[1])
                print("             ") #for spacing 
                
    if counter == 0:#message to user if no books are found
        print("There are no books between the given years")
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



