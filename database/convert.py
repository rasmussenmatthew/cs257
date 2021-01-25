#Claire Williams & Matthew Rasmussen
#1/26/2021
#Moves info from one CSV file to other CSV files

#dictionary full of info
import csv

def make_athletes_table():
    #read the CSV 
    #populate dictionary w/ names as keys
    #other info as a list of things
    #write dict into new CSV file
    athlete_dict = {}
    with open('athlete_events.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            name = row[1]
            sex = row[2]
            age = row[3]
            height = row[4]
            weight = row[5]
            if name not in athlete_dict:
                athlete_dict[name] = [sex, age, height, weight]
    #print(athlete_dict)
    with open('athletes.csv', 'w', newline='') as new_csv_file:
        writer = csv.writer(new_csv_file, delimiter=',')
        for key in athlete_dict:
            writer.writerow([key, athlete_dict[key][0], athlete_dict[key][1], athlete_dict[key][2], athlete_dict[key][3]])

def main():
    make_athletes_table()
    
main()