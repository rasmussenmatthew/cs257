#Nacho Rodriguez-Cortes & Matthew Rasmussen
#2/21/2021
#Moves info from one CSV file to other CSV files

import csv

def make_spells_table():
    ''' 
    Reads the "spells.csv", writes a new "spells_new.csv" file.
    '''
    spell_dict = {}
    
    with open('spells.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
            spell_name = row[3]
            spell_description = row[4]
            higher_level = row[5]
            components = row[7]
            material = row[8]
            ritual = row[9]
            duration = row[10]
            concentration = row[11]
            casting_time = row[12]
            spell_level = row[13]
            attack_type = row[14]
            damage_information = row[15]
            school = row[16]
            classes = row[17]
            dc_information = row[20]
            heal_at_level = row[21]
            if spell_name not in spell_dict:
                spell_dict[spell_name] = [len(spell_dict) + 1, spell_description, higher_level, components, material, ritual, duration, concentration, casting_time, spell_level, attack_type, damage_information, school, classes, dc_information, heal_at_level]
                
    with open('spells_new.csv', 'w', newline='') as new_csv_file:
        writer = csv.writer(new_csv_file, delimiter=',')
        for key in spell_dict:
            writer.writerow([spell_dict[key][0], key, spell_dict[key][1], spell_dict[key][2], spell_dict[key][3], spell_dict[key][4], spell_dict[key][5], spell_dict[key][6], spell_dict[key][7], spell_dict[key][8], spell_dict[key][9], spell_dict[key][10], spell_dict[key][11], spell_dict[key][12], spell_dict[key][13], spell_dict[key][14], spell_dict[key][15]])
    
    return spell_dict  

def make_spell_measurments_table():
    ''' 
    Reads the "spells.csv", writes a new "spell_measurments.csv" file.
    '''
    spell_dict = {}
    
    with open('spells.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        spell_id = 1
        for row in csv_reader:
            spell_range = row[6]
            if row[22] != "":
                split_string = row[22].split(',')
                first_half = split_string[0]
                second_half = split_string[1]

                split_string = first_half.split(':')
                effect_shape = split_string[1]
                effect_shape = effect_shape[2:-1]

                split_string = second_half.split(':')
                effect_range = split_string[1]
                effect_range = effect_range[:-1]

            else:
                effect_range = None
                effect_shape = None 

            if spell_id not in spell_dict:
                spell_dict[spell_id] = [spell_range, effect_shape, effect_range]
                spell_id += 1
                                
    with open('spell_measurments.csv', 'w', newline='') as new_csv_file:
        writer = csv.writer(new_csv_file, delimiter=',')
        for key in spell_dict:
            writer.writerow([key, spell_dict[key][0], spell_dict[key][1], spell_dict[key][2]])
    
    return spell_dict 



def main():
    spell_dict = make_spells_table()
    spell_measurments_dict = make_spell_measurments_table()

main()