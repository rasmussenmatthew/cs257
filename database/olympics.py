#Matthew Rasmussen
#1/29/2021
#Implements three ways of searching through the olympics database

import psycopg2
from config import password
from config import database
from config import user
import csv
import argparse


def get_parsed_arguments():
    '''
        Takes in user input and returns parsed arguments
    '''
    parser = argparse.ArgumentParser(description = 'Search methods for the olympics database')
    parser.add_argument('-a', '--athletes', type = str, metavar=' ', help = 'prints a list of every athlete from a specified NOC (search string)')
    parser.add_argument('-gc', '--gold_count', action = 'store_true', help = 'prints a list of every NOC and a count of gold medals won by their respective representatives')
    parser.add_argument('-avg', '--height_average', action = 'store_true', help = 'prints the average height of the participants in every sport')
    parser.add_argument('-u', '--usage', action = 'store_true', help = 'prints the entire usage statement')
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
        query = '''SELECT DISTINCT athletes.athlete_name, nations.NOC 
                    FROM athletes_games, athletes, nations 
                    WHERE athletes.id = athletes_games.athlete_id 
                    AND nations.id = athletes_games.nation_id 
                    AND nations.NOC = %s 
                    ORDER BY athlete_name;'''
        cursor.execute(query, (search_string,))
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
        Print the tally of gold medals won by representatives of each NOC
    '''
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = '''SELECT nations.NOC, COUNT(contests_medals.medal)
                    FROM nations, athletes_games, contests_medals
                    WHERE athletes_games.id = contests_medals.athletes_games_id
                    AND nations.id = athletes_games.nation_id
                    AND contests_medals.medal = 'Gold'
                    GROUP BY nations.NOC
                    ORDER BY COUNT(contests_medals.medal) DESC;'''  
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    print('===== Count of Gold Medals Won by each NOC ====')
    for row in cursor:
        print(row[0], "|", row[1])
    print()

    connection.close()

def find_avg_height():
    '''
        Print the average height of the participants in every sport
    '''
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = '''SELECT contests.sport, AVG(athletes.height)
                    FROM contests, athletes_games, contests_medals, athletes
                    WHERE athletes.id = athletes_games.athlete_id
                    AND athletes_games.id = contests_medals.athletes_games_id
                    AND contests.id = contests_medals.contest_id
                    GROUP BY contests.sport
                    ORDER BY contests.sport;'''  
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    print('===== Average Height of Participants for Every Sport (cm) ====')
    for row in cursor:
        print(row[0], "|", row[1])
    print()

    connection.close()

def print_usage():
    with open("usage.txt") as usage_file:
        for line in usage_file:
            print(line)

def main():
    args = get_parsed_arguments()
    if args.athletes != None:
        find_athletes(args.athletes)
    if args.gold_count:
        find_gold_count()
    if args.height_average:
        find_avg_height() 
    if args.usage:
        print_usage()

if __name__ == "__main__":
    main()