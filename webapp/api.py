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
        query = 'SELECT spell_name, spell_level, casting_time, ritual FROM spells'
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    spells_list = []
    for row in cursor:
        spells_dictionary = {'spell_name' : row[0], 'spell_level' : row[1], 'casting_time' : row[2], 'ritual' : row[3]}
        spells_list.append(spells_dictionary)
        
    connection.close()
    return json.dumps(spells_list)

@api.route('/spells/<spell_name>')
def get_spell_information(spell_name):
    like_arguments = spell_name
    query = '''SELECT * FROM spells WHERE spell_name LIKE %s'''

    spells_list = []

    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        cursor = connection.cursor()
        cursor.execute(query, [like_arguments])
        for row in cursor:
            spells_dictionary = {'spell_name' : row[1], 'spell_description' : row[2], 'higher_level' : row[3], 'components' : row[4], 'material' : row[5], 'ritual' : row[6], 'duration' : row[7], 'concentration' : row[8], 'casting_time' : row[9], 'spell_level' : row[10], 'attack_type' : row[11], 'damage_information' : row[12], 'school' : row[13], 'classes' : row[14], 'dc_information' : row[15], 'heal_at_level' : row[16]}
            spells_list.append(spells_dictionary)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e)
        exit()
        
    return json.dumps(spells_list)


@api.route('/spells/classes/<class_name>')
def get_spells_for_class(class_name):
    # Pay special attention to quotes! Originally not working when using single quotes on outside and double quotes for like clause
    like_arguments = '%' + class_name + '%'
    query = '''SELECT spell_name, spell_level, casting_time, ritual 
               FROM spells 
               WHERE classes LIKE %s''' 
    spells_list = []

    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        cursor = connection.cursor()
        cursor.execute(query, [like_arguments])
        for row in cursor:
            spells_dictionary = {'spell_name' : row[0], 'spell_level' : row[1], 'casting_time' : row[2], 'ritual' : row[3]}
            spells_list.append(spells_dictionary)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e)
        exit()
        
    return json.dumps(spells_list)
 
@api.route('/help')
def get_help():
  return '''
        REQUEST: /spells <br>
        <br>
        RESPONSE: a JSON list of dictionaries containing the essential information for every spell. <br>
        <br>
        Here are the fields for each spell: <br>
            name -- (string) the name of the spell  <br>
            spell level -- (string) the base level needed to cast the spell <br>
            casting time -- (string) describes the time needed to cast the spell <br>
            ritual -- (boolean) says whether or not the spell requires a ritual  <br>
        <br>
        REQUEST: /spells/<spell_name>
        <br>
        RESPONSE: a JSON list of dictionaries containing all the information for a specific spell. <br>
        <br>
        Here are the some of the fields for each spell: <br>
            name -- (string) the name of the spell  <br>
            spell level -- (string) the base level needed to cast the spell <br>
            casting time -- (string) describes the time needed to cast the spell <br>
            ritual -- (boolean) says whether or not the spell requires a ritual  <br>
            spell description -- (string) a description of the effects of the spell <br>
        <br>
        REQUEST: /spells/classes/<class_name>
        <br>
        RESPONSE: a JSON list of dictionaries containing the essential information for every spell from a certain class. <br>
        <br>
        The response is the same as that for the /spells/ request.
        <br>
        Here are the fields for each spell: <br>
            name -- (string) the name of the spell  <br>
            spell level -- (string) the base level needed to cast the spell <br>
            casting time -- (string) describes the time needed to cast the spell <br>
            ritual -- (boolean) says whether or not the spell requires a ritual  <br>
         '''



