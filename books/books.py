#Eric Gassel & Matthew Rasmussen 
#1/22/2021
#Revised by both Eric Gassel & Matthew Rasmussen

import csv
import argparse

def get_parsed_arguments():
    '''Takes in user input and returns parsed arguments'''
    
    parser = argparse.ArgumentParser(description = 'Multiple ways to search through a csv file of authors and their books')
    parser.add_argument('-a', '--authors', type = str, metavar=' ', help = 'prints a list of every author who contains given search string and prints a list of each author\'s books')
    parser.add_argument('-t', '--titles', type = str, metavar='', help = 'prints a list of every book whose title contains given string')
    parser.add_argument('-y', '--years', nargs = 2, type = int, metavar='', help = 'prints a list of every book published between input year A and B, inclusive')
    parser.add_argument('-u', '--usage', action= 'store_true', help = 'prints the entire usage statement')
    args = parser.parse_args()
    
    return args
 
def find_authors(authors): 
    '''Returns a dictionary of all authors that contain the search string along with a list of their books.'''
    
    author_dict = {} 
    search_string = str(authors).lower()
    with open('books.csv') as csv_file:
        csv_reader= csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            author = row[2]
            author_book = row[0]
            if search_string in author.lower():
                if author not in author_dict: 
                    author_dict[author] = [author_book]
                else:
                    author_dict[author].append(author_book)
   
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
    if years[0] > years[1]: 
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

def print_dict_results(dictionary):
    if not dictionary:
        print("There is no book who meets the search criteria. \n") 
    else:    
        for key in dictionary: 
            author = str(key) 
            print("-",author) 
            key_list = dictionary[key]
            for i in range(len(dictionary[key])):
                print(" " * 5, key_list[i])
            print("")
    print("-" * 100)
    
    return 
        
def print_list_results(result_list):
    if not result_list:
        print("There is no book who meets the search criteria. \n") 
    else:
        for book_info in result_list:
            title = book_info[0]
            author = book_info[1]
            pub_year = book_info[2]
            print(title,"(", pub_year, "), written by", author, "\n")
    print("-" * 100)
            
    return

def main():
    args = get_parsed_arguments()
    if args.authors != None:
        print_dict_results(find_authors(args.authors))
    if args.titles != None:
        print_list_results(find_titles(args.titles))
    if args.years != None:
        print_list_results(find_years(args.years))
    if args.usage:
        print_usage()

if __name__ == "__main__":
    main()



