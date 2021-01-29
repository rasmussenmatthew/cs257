#Matthew Rasmussen
#1/29/2021
#This does things from the command line with my database 

from config import password
from config import database
from config import user
import csv
import argparse


def get_parsed_arguments():
    '''Takes in user input and returns parsed arguments'''
    
    parser = argparse.ArgumentParser(description = 'Search methods for the olympics database')
    parser.add_argument('-a', '--athletes', type = str, metavar=' ', help = 'prints a list of every athlete from a specified NOC (search string)')
    parser.add_argument('-gc', '--gold_count', type = str, metavar='', help = 'prints a list of every NOC and a count of gold medals one by their respective representatives')
    parser.add_argument('-avg', '--average_age', type = str, metavar='', help = 'prints the average age of the participants in every sport')
    parser.add_argument('-u', '--usage', action= 'store_true', help = 'prints the entire usage statement')
    args = parser.parse_args()
    
    return args

def find_athletes(athletes):
    '''
        Returns or prints a list of athletes from a specified NOC
    '''
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()
    
    search_string = athletes
    try:
        cursor = connection.cursor()
        query = '''SELECT DISTINCT athletes.athlete_name, nations.NOC FROM nations, athletes_games, athletes WHERE athletes.id = athletes_games.athlete_id AND nations.id = athletes_games.nation_id AND nations.NOC = '%s' ORDER BY athlete_name;'''
        cursor.execute(query, (search_string))
    except Exception as e:
        print(e)
        exit()

    print('===== All athletes from {0}===='.format(search_string))
    for row in cursor:
        print(row[0])
    print()

    connection.close()


def find_gold_count():
    '''
        Print the tally of gold medals one by representatives of each NOC
    '''
    return 

def find_avg_age():
    '''
        Print the average age of the participants in every sport
    '''
    return 

#def print_usage():
 #   with open("usage.txt") as usage_file:
  #      for line in usage_file:
   #         print(line)
            
    #return
''' 

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
'''
def main():
    args = get_parsed_arguments()
    if args.athletes != None:
        #print_dict_results(find_athletes(args.athletes))
    if args.gold_count != None:
        #print_list_results(find_gold_count(args.gold_count))
    if args.average_age != None:
        #print_list_results(find_avg_age(args.average_age))
    if args.usage:
        print_usage()

if __name__ == "__main__":
    main()