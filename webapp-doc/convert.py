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
    

def make_weapon_table():
    weapon_dict = {}

    with open('equipment.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
            if "weapon" in row[4]:
                weapon_name = row[3]
                cost = row[6]
                weight = row[7]
                weapon_category = row[13]

                if row[16] != "":
                    split_string_dmg = row[16].split(',')
                    first_section = split_string_dmg[0]
                    last_section = split_string_dmg[2]
                    split_string_dmg = first_section.split(':')
                    damage_die = split_string_dmg[1]
                    #damage_die = damage_die[2:-1]
                    split_string_dmg = last_section.split(':')
                    damage_type = split_string_dmg[1]
                    #damage_type = long_range[:-1]

                properties = []
                properties_string = row[18]
                #ammunition and loading are 'name :' first
                properties_string = properties_string.split(',')
                for split_string in range(len(properties_string)):
                    if split_string % 2 != 0:
                        if 'loading' in properties_string[split_string]:
                            properties.append('Loading')
                        if 'ammunition' in properties_string[split_string]:
                            properties.append('Ammunition')
                        else:
                            new_split = properties_string[split_string].split(':')
                            properties.append(new_split[1])
                
                split_string_2h_dmg = row[19]
                if split_string_2h_dmg != "":
                    split_string_2h_dmg = split_string_2h_dmg.split(',')
                    first_section = split_string_2h_dmg[0]
                    split_string_2h_dmg = first_section.split(':')
                    two_handed_dmg = split_string_2h_dmg[1]
                    #two_handed_dmg = two_handed_dmg[2:-1]

                if weapon_name not in weapon_dict:
                    weapon_dict[weapon_name] = [len(weapon_dict) + 1, cost, weight, weapon_category, damage_die, damage_type, properties, two_handed_dmg]
                
    with open('weapons_new.csv', 'w', newline='') as new_csv_file:
        writer = csv.writer(new_csv_file, delimiter=',')
        for key in weapon_dict:
            writer.writerow([weapon_dict[key][0], key, weapon_dict[key][1], weapon_dict[key][2], weapon_dict[key][3], weapon_dict[key][4], weapon_dict[key][5], weapon_dict[key][6], weapon_dict[key][7]])  

def make_weapon_range_table():
    weapon_dict = {}
    with open('equipment.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        spell_id = 1
        for row in csv_reader:
            if "weapon" in row[4]:
                if row[17] != "":
                    split_string = row[17].split(',')
                    first_half = split_string[0]
                    second_half = split_string[1]

                    split_string = first_half.split(':')
                    normal_range = split_string[1]
                    #normal_range = normal_range[2:-1]

                    split_string = second_half.split(':')
                    long_range = split_string[1]
                    long_range = long_range[:-1]

                if len(weapon_dict)+1 not in weapon_dict:
                    weapon_dict[len(weapon_dict)+1] = [normal_range, long_range]
                    spell_id += 1
                                
    with open('weapon_range.csv', 'w', newline='') as new_csv_file:
        writer = csv.writer(new_csv_file, delimiter=',')
        for key in weapon_dict:
            writer.writerow([key, weapon_dict[key][0], weapon_dict[key][1]])


def make_armor_table(): 
    armor_dict = {}
  
    with open('equipment.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
            if "armor" in row[4]:
                armor_name = row[3]
                cost_info = row[6]
                if cost_info != "":
                    split_string = cost_info.split(',')
                    first_half = split_string[0]
                    second_half = split_string[1]

                    split_string = first_half.split(':')
                    cost_quantity = split_string[1]
    
                    split_string = second_half.split(':')
                    cost_unit = split_string[1]
                    cost_unit = cost_unit[:-1]
      
                    cost = cost_quantity + cost_unit
                else:
                    cost = None
                weight = row[7]
                str_minimum = row[22]
                stealth_disadvantage = row[23]
                armor_class = row[21]
                armor_category = row[20]
                if armor_class != "":
                    split_string = armor_class.split(',')
                    first_third = split_string[0]
                    second_third = split_string[1]
                    third_third = split_string[2]

                    split_string = first_third.split(':')
                    base_armor_class = split_string[1]

                    split_string = second_third.split(':')
                    dex_bonus = split_string[1]

                    split_string = second_third.split(':')
                    max_bonus = split_string[1]

                else:
                    base_armor_class = None
                    dex_bonus = None
                    max_bonus = None

                if armor_name not in armor_dict:
                    armor_dict[armor_name] = [cost, weight, str_minimum, stealth_disadvantage, base_armor_class, dex_bonus, max_bonus, armor_category] 
 
    with open('armor_new.csv', 'w', newline = '') as new_csv_file:
        writer = csv.writer(new_csv_file, delimiter=',')
        for key in armor_dict:
            writer.writerow([key, armor_dict[key][0], armor_dict[key][1], armor_dict[key][2], armor_dict[key][3], armor_dict[key][4], armor_dict[key][5], armor_dict[key][6], armor_dict[key][7]])

def make_tools_table():
    tools_dict = {}
  
    with open('equipment.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
            if "tools" in row[4]:
                tool_name = row[3]
                cost_info = row[6]
                if cost_info != "":
                    split_string = cost_info.split(',')
                    first_half = split_string[0]
                    second_half = split_string[1]

                    split_string = first_half.split(':')
                    cost_quantity = split_string[1]
      
                    split_string = second_half.split(':')
                    cost_unit = split_string[1]
                    cost_unit = cost_unit[:-1]
                    
                    cost = cost_quantity + cost_unit
                else:
                    cost = None
                weight = row[7]
                tool_category = row[10]
                tool_description = row[9]
                tool_description = tool_description[1:-1]
                    
                if tool_name not in tools_dict:
                    tools_dict[tool_name] = [cost, weight, tool_description, tool_category]
    with open('tools_new.csv', 'w', newline = '') as new_csv_file:
        writer = csv.writer(new_csv_file, delimiter=',')
        for key in tools_dict:
            writer.writerow([key, tools_dict[key][0], tools_dict[key][1], tools_dict[key][2], tools_dict[key][3]])

def make_gear_table():
    gear_dict = {}
  
    with open('equipment.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
            if "gear" in row[4]:
                gear_name = row[3]
                cost_info = row[6]
                if cost_info != "":
                    split_string = cost_info.split(',')
                    first_half = split_string[0]
                    second_half = split_string[1]

                    split_string = first_half.split(':')
                    cost_quantity = split_string[1]
                    
                    split_string = second_half.split(':')
                    cost_unit = split_string[1]
                    cost_unit = cost_unit[:-1]
      
                    cost = cost_quantity + cost_unit
                else:
                    cost = None
                weight = row[7]
                gear_description = row[9]
                gear_description = gear_description[1:-1]
                gear_quantity = row[12]
                
                if gear_name not in gear_dict:
                    gear_dict[gear_name] = [cost, weight, gear_description, gear_quantity]

    with open('gear_new.csv', 'w', newline = '') as new_csv_file:
        writer = csv.writer(new_csv_file, delimiter=',')
        for key in gear_dict:
            writer.writerow([key, gear_dict[key][0], gear_dict[key][1], gear_dict[key][2], gear_dict[key][3]])

def make_mounts_table():
    mounts_dict = {}
  
    with open('equipment.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
            if "mounts" in row[4]:
                mount_name = row[3]
                cost_info = row[6]
                if cost_info != "":
                    split_string = cost_info.split(',')
                    first_half = split_string[0]
                    second_half = split_string[1]

                    split_string = first_half.split(':')
                    cost_quantity = split_string[1]
                    
                    split_string = second_half.split(':')
                    cost_unit = split_string[1]
                    cost_unit = cost_unit[:-1]
      
                    cost = cost_quantity + cost_unit
                else:
                    cost = None
                weight = row[7]
                vehicle_category = row[11]
                speed = row[25]
                speed = speed[1:-1]
                if speed != "":
                    split_string = speed.split(',')
                    first_half = split_string[0]
                    second_half = split_string[1]

                    split_string = first_half.split(':')
                    speed_quantity = split_string[1]
       
                    split_string = second_half.split(':')
                    speed_unit = split_string[1]
                    
                    speed = speed_quantity + speed_unit
                else:
                    speed = None
                capacity = row[26]
                
                if mount_name not in mounts_dict:
                    mounts_dict[mount_name] = [cost, weight, vehicle_category, speed, capacity]

    with open('mounts_new.csv', 'w', newline = '') as new_csv_file:
        writer = csv.writer(new_csv_file, delimiter=',')
        for key in mounts_dict:
            writer.writerow([key, mounts_dict[key][0], mounts_dict[key][1], mounts_dict[key][2], mounts_dict[key][3], mounts_dict[key][4]])

make_spells_table()
make_spell_measurments_table()
make_weapon_table()
make_weapon_range_table()
make_armor_table()
make_tools_table()
make_gear_table()
make_mounts_table()
