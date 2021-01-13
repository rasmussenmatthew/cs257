#Eric Gassel & Matthew Rasmussen 

import csv

author_dict = {} 

#reading in csv file
with open('books.csv') as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',')
    #filling the dictionary to connect a list of books to each author
    for row in csv_reader:
        if {row[2]} not in author_dict: #no repeats
            author_dict[{row[2]}] = [{row[0]}]
        else:
            author_dict[{row(2)}].append({row[0]})

    
def authors(name): #authors command
    for key in author_dict{}:
        author= str(key) #jic key is not string 
        if lower(name) in lower(author):
            print("-",author)
            print("   ",author_dict[key])
    return

def titles(name): #titles command
    return true

def years(year1, year2):
    #names command
    return true

def help1():
    #print statement TBD
    return true

#NICE

def main():
    print("hello")
main()

