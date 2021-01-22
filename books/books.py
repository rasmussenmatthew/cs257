#Eric Gassel & Matthew Rasmussen 

import csv
import argparse


def get_parsed_arguments():
    '''setting up parser and arguments''' #HEYYYYYY FIX THIS
    
    parser = argparse.ArgumentParser(description = 'Multiple ways to search through a csv file of authors and their books')

    parser.add_argument('-a', '--authors', type = str, metavar='', help = 'prints a list of every author who contains given search string and prints a list of each author\'s books')
    parser.add_argument('-t', '--titles', type = str, metavar='', help = 'prints a list of every book whose title contains given string')
    parser.add_argument('-y', '--years', nargs = 2, type = int, metavar='', help = 'prints a list of every book published between input year A and B, inclusive')
    parser.add_argument('-u', '--usage', action= 'store_true', help = 'prints the entire usage statement')

    args = parser.parse_args()
    
    return args

    
def find_authors(authors): 
    '''Returns a dictionary of all authors that contain the search string along with a list of their books.'''
    
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
    
    return author_dict

def find_titles(titles): 
    '''Returns a list of all titles that contain the search string along with its author and publish year.'''
    
    titles_list = []
    with open('books.csv') as csv_file:
        csv_reader= csv.reader(csv_file, delimiter=',')
        for row in csv_reader: 
            if titles.lower() in row[0].lower():
                temp_list=[row[0],row[2],row[1]]
                titles_list.append(temp_list)    
                
    return titles_list

def find_years(years): 
    '''Returns a list of all books that were published between the search years along with its author.'''
    
    publish_list = []
    
    if years[0] > years[1]: #ordering years so the smaller comes first
        years_small = years[1]
        years_big = years[0]
    else:                   
        years_big = years[1]
        years_small = years[0]

    with open('books.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            book_year = int(row[1])
            if book_year >= years_small and book_year <= years_big:
                temp_list=[row[0],row[2],row[1]]
                publish_list.append(temp_list) 
                
    return publish_list

def print_usage():
    with open("usage.txt") as usage_file:
        for line in usage_file:
            print(line)
            
    return

def print_search_results(results, args):
    
    if args.authors != None:
        counter = 0
        search_author = str(args.authors).lower()
        author_dict = results
        for key in author_dict: #looping through dictionary
            author= str(key) #changing author (including lifespans) to string
            if search_author in author.lower():
                counter += 1
                print("-",author) #for spacing 
                key_list = author_dict[key]
                for i in range(len(author_dict[key])):
                    print(" " * 5, key_list[i])
                print("")
        if counter == 0:
            print("There is no author whose name conatins the given string. \n")
        
        
    if args.titles != None:
        titles_list = results
        if not titles_list:
            print("There is no book whose title contains the given string. \n") 
        else:
            for book_info in titles_list:
                title = book_info[0]
                author = book_info[1]
                pub_year = book_info[2]
                print(title,"(", pub_year, "), written by", author, "\n")
            
    if args.years != None:
        publish_list = results
        if not publish_list:
            print("There is no book whose published year is within your search years. \n") 
        else:
            for book_info in publish_list:
                title = book_info[0]
                author = book_info[1]
                pub_year = book_info[2]
                print(title,"(", pub_year, "), written by", author, "\n")
                
    return

def main():
    args = get_parsed_arguments()
    #if statments to see which function is being used
    if args.authors != None:
        print_search_results(find_authors(args.authors), args)
    if args.titles != None:
        print_search_results(find_titles(args.titles), args)
    if args.years != None:
        print_search_results(find_years(args.years), args)
    if args.usage:
        print_usage()

if __name__ == "__main__":
    main()



