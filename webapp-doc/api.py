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

@api.route('/spells/classes/<class_name>')
def get_spells_for_class(class_name):
    # Pay special attention to quotes! Originally not working when using single quotes on outside and double quotes for like clause
    like_arguments = '%' + class_name + '%'
    query = '''SELECT spell_name, spell_description, components, ritual 
               FROM spells 
               WHERE classes LIKE %s LIMIT 10 ''' 
    spells_list = []

    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        cursor = connection.cursor()
        cursor.execute(query, [like_arguments])
        for row in cursor:
            spells_dictionary = {'spell_name' : row[0], 'spell_description' : row[1], 'components' : row[2], 'ritual' : row[3]}
            spells_list.append(spells_dictionary)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e)
        exit()
    '''
    spells_list = [{'spell_name':'acid arrow', 'spell_description':'fire an acid arrow', 'components':'[v,s]', 'ritual':'FALSE'},
                    {'spell_name':'fireball', 'spell_description':'giant exploding ball of fire', 'components':'[v,s]', 'ritual':'FALSE'}]
    '''
    return json.dumps(spells_list)

@api.route('/equipment')
def get_equipment():
    equipment_list = []
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        cursor = connection.cursor()
        query = '''SELECT tools.name, tools.cost, tools.weight FROM tools'''
        cursor.execute(query)
        for row in cursor:
            equipment_dictionary = {'tool_name' : row[0], 'tool_cost' : row[1], 'tool_weight' : row[2]}
            equipment_list.append(equipment_dictionary)
     
    except Exception as e:
        print(e)
        exit()
    connection.close()
    return json.dumps(equipment_list)
 

