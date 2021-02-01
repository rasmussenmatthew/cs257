#Harry Tian and Matthew Rasmussen 
#2/2/2021
#API for olympics database

from config import password
from config import database
from config import user

import psycopg2
import flask
import json
import argparse

app = flask.Flask(__name__)


@app.route('/games')
def get_games():
    '''
        a JSON list of dictionaries, each of which represents one
        Olympic games, sorted by year. Each dictionary in this list will have
        the following fields.

        id -- (INTEGER) a unique identifier for the games in question
        year -- (INTEGER) the 4-digit year in which the games were held (e.g. 1992)
        season -- (TEXT) the season of the games (either "Summer" or "Winter")
        city -- (TEXT) the host city (e.g. "Barcelona") 
    '''
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = 'SELECT id, game_year, season, city FROM games ORDER BY game_year'
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()
    
    results_list = []

    for row in cursor:
        games_dictionary = {'id': row[0], 'year' : row[1], 'season' : row[2], 'city' : row[3]}
        results_list.append(games_dictionary)
    
    return json.dumps(results_list)

@app.route('/noc')
def get_noc():
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = 'SELECT NOC, team FROM nations ORDER BY NOC'
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    results_list = []
    for row in cursor:
        nations_dictionary = {'NOC' : row[0], 'region' : row[1]}
        results_list.append(nations_dictionary)
    
    return json.dumps(results_list)


@app.route('/medalists/games/<games_id>?[noc=noc_abbreviation]')
def get_medalists(games_id):
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()
    games_id = games_id
    noc = flask.request.args.get('noc')
    if noc is not None:
        try:
            cursor = connection.cursor()
            query = '''SELECT DISTINCT athletes.id, athletes.athlete_name, athletes.sex, 
                    contests.sport, contests.contest, contests_medals.medal 
                    FROM athletes, contests_medals, athletes_games, contests, games
                    WHERE athletes.id = athletes_games.athlete_id
                    AND games.id = %s
                    AND games.id = athletes_games.game_id
                    AND athletes_games.id = contests_medals.athletes_games_id
                    AND contests_medals.medal IS NOT NULL
                    AND nations.id = athletes_games.nation_id
                    AND contests.id = contests_medals.contest_id;'''
            cursor.execute(query, (games_id,))
        except Exception as e:
            print(e)
            exit()
    else:
        try:
            cursor = connection.cursor()
            query = '''SELECT DISTINCT athletes.id, athletes.athlete_name, athletes.sex, 
                    contests.sport, contests.contest, contests_medals.medal 
                    FROM athletes, contests_medals, athletes_games, contests, games
                    WHERE athletes.id = athletes_games.athlete_id
                    AND games.id = %s
                    AND games.id = athletes_games.game_id
                    AND athletes_games.id = contests_medals.athletes_games_id
                    AND contests_medals.medal IS NOT NULL
                    AND contests.id = contests_medals.contest_id;'''
            cursor.execute(query, (games_id,))
        except Exception as e:
            print(e)
            exit()

    results_list = []
    for row in cursor:
        nations_dictionary = {'athleteid':row[0], 'athletename':row[1], 'athletesex':row[3], 'sport':row[4], 'event':[5], 'medal':row[6]}
        results_list.append(nations_dictionary)

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)