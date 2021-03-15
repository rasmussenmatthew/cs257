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
         REQUEST: /  <br>
         <br>            
         RESPONSE: a JSON list of dictionaries each of which containing the title of our tables. <br>
         <br>
         REQUEST: /equipment  <br>
         <br>
         RESPONSE: a JSON list of dictionaries containing the essential information for every piece of equpimenmt <br>
         <br>
         Here are the fields for one of the sections of equipment (Tools): <br>
           name -- (string) the name of the tool  <br>
           cost -- (integer) the cost for the tool <br>
           weight -- (integer) the amount the tool weighs <br>
         <br>
         REQUEST: /spells <br>
         <br>
         RESPONSE: a JSON list of dictionaries containing the essential information for every spell. <br>
         <br>
         Here are the fields for each spell: <br>
           name -- (string) the name of the spell  <br>
           description -- (string) Describes the spell <br>
           components -- (string) Lists the components required to perform the spell (i.e (V) for Verbal) <br>
           ritual -- (boolean) says whether or not the spell requires a ritual  <br>



         '''



