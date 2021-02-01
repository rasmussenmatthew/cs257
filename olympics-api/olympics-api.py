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
    games_dictionary = {}
    for row in cursor:
        games_dictionary = {'id' = row[0], 'year' = row[1], 'season' = row[2], 'city' = row[3]}\
        results_list.append(games_dictionary)
    
    return json.dumps(results_list)

@app.route('/noc')
def get_noc():
 '''
    a JSON list of dictionaries, each of which represents one
    National Olympic Committee, alphabetized by NOC abbreviation. Each dictionary
    in this list will have the following fields.


    abbreviation -- (TEXT) the NOC's abbreviation (e.g. "USA", "MEX", "CAN", etc.)
    name -- (TEXT) the NOC's full name (see the noc_regions.csv file)
 '''
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()


@app.route('/medalists/games/<games_id>?[noc=noc_abbreviation]')
def get_medalists(games_id, noc):
 '''
    a JSON list of dictionaries, each representing one athlete
    who earned a medal in the specified games. Each dictionary will have the
    following fields.

    athlete_id -- (INTEGER) a unique identifier for the athlete
    athlete_name -- (INTEGER) a unique identifier for the athlete
    athlete_sex -- (TEXT) the athlete's sex as specified in the database ("F" or "M")
    sport -- (TEXT) the name of the sport in which the medal was earned
    event -- (TEXT) the name of the event in which the medal was earned
    medal -- (TEXT) the type of medal ("gold", "silver", or "bronze")

    If the GET parameter noc=noc_abbreviation is present, this endpoint will return
    only those medalists who were on the specified NOC's team during the specified
    games.
 '''
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)