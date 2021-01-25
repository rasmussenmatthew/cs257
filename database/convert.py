#Claire Williams & Matthew Rasmussen
#1/26/2021
#Moves info from one CSV file to other CSV files

#dictionary full of info
import csv

def make_athletes_table():
    '''SOMETHING '''
    athlete_dict = {}
    
    with open('athlete_events.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            name = row[1]
            sex = row[2]
            age = row[3]
            height = row[4]
            weight = row[5]
            if name != "Name":
                if name not in athlete_dict:
                    athlete_dict[name] = [sex, age, height, weight]
                
    with open('athletes.csv', 'w', newline='') as new_csv_file:
        writer = csv.writer(new_csv_file, delimiter=',')
        for key in athlete_dict:
            writer.writerow([key, athlete_dict[key][0], athlete_dict[key][1], athlete_dict[key][2], athlete_dict[key][3]])

def make_nations_table():
    list_of_nations = []
    with open ('noc_regions.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            noc = row[0]
            region = row[1]
            if noc != "NOC":
                list_of_nations.append([noc, region])
    
    with open('nations.csv', 'w', newline='') as new_csv_file:
        writer = csv.writer(new_csv_file, delimiter=',')
        for nation in list_of_nations:
            writer.writerow(nation)
            
#def make_games_table():
    
#def make_contests_table():



def main():
    #make_athletes_table()
    make_nations_table()
    
main()