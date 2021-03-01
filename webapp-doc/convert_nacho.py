def make_armor_table(): 
  armor_dict = {}
  
  with open('equipment.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
            armor_name = row[2]
            cost_info = row[5]
            if cost_info != "":
                split_string = cost_info.split(',')
                first_half = split_string[0]
                second_half = split_string[1]

                split_string = first_half.split(':')
                cost_quantity = split_string[1]
                
                split_string = second_half.split(':')
                cost_unit = split_string[1]
      
                cost = str(cost_quantity) + cost_unit
            else:
                cost = None
            weight = row[6]
            str_minimum = row[21]
            stealth_disadvantage = row[22]
            armor_class = row[20]
            armor_category = row[19]
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
                class_base = None
                dex_bonus = None
                max_bonus = None

            if armor_name not in armor_dict:
                armor_dict[armor_name] = [cost, weight, str_minimum, stealth_disadvantage, base_armor_class, dex_bonus, max_bonus, armor_category] 
 
  with open('armor_new.csv', 'w', newline = '') as new_csv_file:
      writer = csv.writer(new_csv_file, delimiter=',')
      for key in armor_dict:
          writer.writerow([armor_dict[key][0], armor_dict[key][1], armor_dict[key][2], armor_dict[key][3], armor_dict[key][4], armor_dict[key][5], armor_dict[key][6], armor_dict[key][7],  armor_dict[key][8]])

def make_tools_table():
   tools_dict = {}
  
  with open('equipment.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
            tool_name = row[2]
            cost_info = row[5]
            if cost_info != "":
                split_string = cost_info.split(',')
                first_half = split_string[0]
                second_half = split_string[1]

                split_string = first_half.split(':')
                cost_quantity = split_string[1]
                
                split_string = second_half.split(':')
                cost_unit = split_string[1]
      
                cost = str(cost_quantity) + cost_unit
            else:
                cost = None
            weight = row[6]
            tool_category = row[9]
            tool_description = row[8]
            
            if tool_name not in tools_dict:
                tools_dict[tool_name] = [cost, weight, tool_description, tool_category]
  with open('tools_new.csv', 'w', newline = '') as new_csv_file:
      writer = csv.writer(new_csv_file, delimiter=',')
      for key in tools_dict:
          writer.writerow([tools_dict[key][0], tools_dict[key][1], tools_dict[key][2], tools_dict[key][3], tools_dict[key][4]])

def make_gear_table():
   gear_dict = {}
  
  with open('equipment.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
            gear_name = row[2]
            cost_info = row[5]
            if cost_info != "":
                split_string = cost_info.split(',')
                first_half = split_string[0]
                second_half = split_string[1]

                split_string = first_half.split(':')
                cost_quantity = split_string[1]
                
                split_string = second_half.split(':')
                cost_unit = split_string[1]
      
                cost = str(cost_quantity) + cost_unit
            else:
                cost = None
            weight = row[6]
            gear_description = row[8]
            gear_quantity = row[11]
            
            if gear_name not in gear_dict:
                gear_dict[gear_name] = [cost, weight, gear_description, gear_quantity]
  with open('gear_new.csv', 'w', newline = '') as new_csv_file:
      writer = csv.writer(new_csv_file, delimiter=',')
      for key in gear_dict:
          writer.writerow([gear_dict[key][0], gear_dict[key][1], gear_dict[key][2], gear_dict[key][3], gear_dict[key][4]])

def make_mounts_table():
   mounts_dict = {}
  
  with open('equipment.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
            mount_name = row[2]
            cost_info = row[5]
            if cost_info != "":
                split_string = cost_info.split(',')
                first_half = split_string[0]
                second_half = split_string[1]

                split_string = first_half.split(':')
                cost_quantity = split_string[1]
                
                split_string = second_half.split(':')
                cost_unit = split_string[1]
      
                cost = cost_quantity + cost_unit
            else:
                cost = None
            weight = row[6]
            vehicle_category = row[10]
            speed = row[24]
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
            capacity = row[25]
            
            if mount_name not in mounts_dict:
                mounts_dict[mount_name] = [cost, weight, vehicle_category, speed, capacity]
  with open('mounts_new.csv', 'w', newline = '') as new_csv_file:
      writer = csv.writer(new_csv_file, delimiter=',')
      for key in mounts_dict:
          writer.writerow([mounts_dict[key][0], mounts_dict[key][1], mounts_dict[key][2], mounts_dict[key][3], mounts_dict[key][4]])



