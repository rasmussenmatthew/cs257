'''
    api.py
    Nacho Rodriguez-Cortes, Matthew Rasmussen, 21 February 2020

    Flask API to support the web application.
'''
import sys
import flask
import json
import psycopg2

from config import password
from config import database
from config import user

api = flask.Blueprint('api', __name__)

@api.route('/spells')
def get_spells():
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = 'SELECT spell_name, spell_description, components, ritual FROM spells LIMIT 10'
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    spells_list = []
    for row in cursor:
        spells_dictionary = {'spell_name' : row[0], 'spell_description' : row[1], 'components' : row[2], 'ritual' : row[3]}
        spells_list.append(spells_dictionary)
        
    connection.close()
    '''
    spells_list = [{'spell_name':'acid arrow', 'spell_description':'fire an acid arrow', 'components':'[v,s]', 'ritual':'FALSE'},
                    {'spell_name':'fireball', 'spell_description':'giant exploding ball of fire', 'components':'[v,s]', 'ritual':'FALSE'}]
    '''
    return json.dumps(spells_list)
