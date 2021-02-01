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
    ''' Returns a list of all Olympic games, 
        including their id, year, season and city, sorted by year 
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
    
    connection.close()

    return json.dumps(results_list)

@app.route('/nocs')
def get_noc():
    ''' Returns a list of all NOCs' abbreviations and full names '''
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
        
    connection.close()

    return json.dumps(results_list)


@app.route('/medalists/games/<games_id>')
def get_medalists(games_id):
    '''Returns a list of all athletes who earned medals in the game that matches games_id
       If the GET parameter noc=noc_abbreviation is present, returns only those medalists 
       who were on the specified NOC's team during the specified game
    '''
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    # When GET parameter noc is present
    noc = flask.request.args.get('noc')
    if noc is not None:
        try:
            cursor = connection.cursor()
            query = '''SELECT DISTINCT athletes.id, athletes.athlete_name, athletes.sex, 
                    contests.sport, contests.contest, contests_medals.medal 
                    FROM athletes, contests_medals, athletes_games, contests, games, nations
                    WHERE athletes.id = athletes_games.athlete_id
                    AND games.id = %s
                    AND games.id = athletes_games.game_id
                    AND athletes_games.id = contests_medals.athletes_games_id
                    AND contests_medals.medal IS NOT NULL
                    AND nations.id = athletes_games.nation_id
                    AND nations.noc = %s
                    AND contests.id = contests_medals.contest_id;'''
            cursor.execute(query, (games_id, noc))
        except Exception as e:
            print(e)
            exit()

    # When GET parameter noc is not present
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
        nations_dictionary = {'athlete_id':row[0], 'athlete_name':row[1], 'athlete_sex':row[2], 'sport':row[3], 'event':row[4], 'medal':row[5]}
        results_list.append(nations_dictionary)
    
    connection.close()
    
    return json.dumps(results_list)

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser('Olympics dataset API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
