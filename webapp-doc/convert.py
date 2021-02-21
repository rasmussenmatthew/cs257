#Claire Williams & Matthew Rasmussen
#1/26/2021
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

def main():
    spell_dict = make_spells_table()

main()