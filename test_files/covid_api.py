#Matthew Rasmussen
#1/31/2021
#Test code for api using COVID19 data

'''
 take a state abbreviation (e.g. MN, WA, etc.) 
 as a command-line argument and print out the 
 most recent date's new COVID-19 cases and deaths 
 for that state. 
'''
import sys
import argparse
import json
import urllib.request

API_BASE_URL = 'https://api.covidtracking.com'

def get_covid_data(state):
    '''
    Returns the most recent date's new COVID-19 cases and deaths 
    for the specified state (abreviation)
   
    The state input must be a 2-letter state abreviation
    (e.g. 'OH', 'MN', 'CA', 'NY', etc...)

    Raises exceptions on network connection errors and on data
    format errors.
    '''
    state = str(state).lower()
    url = f'{API_BASE_URL}/v1/states/{state}/current.json'
    data_from_server = urllib.request.urlopen(url).read()
    string_from_server = data_from_server.decode('utf-8')
    covid_data_list = json.loads(string_from_server)
    result_list = []
    new_cases = covid_data_list.get('positiveIncrease', '')
    new_deaths = covid_data_list.get('deathIncrease', '')
    result_list.append(new_cases)
    result_list.append(new_deaths)


    return result_list


def main(args):
    if args.action == 'state':
        covid_data = get_covid_data(args.state)
        print('New cases = ', covid_data[0])
        print('New deaths = ', covid_data[1])
    
if __name__ == '__main__':
    # When I use argparse to parse my command line, I usually
    # put the argparse setup here in the global code, and then
    # call a function called main to do the actual work of
    # the program.
    parser = argparse.ArgumentParser(description='Get state based COVID19 data')

    parser.add_argument('action',
                        metavar='action',
                        help='action to perform on the word (state)',
                        choices=['state'])

    parser.add_argument('state',
                        metavar='state',
                        help='the state as a 2-character abreviation',)


    args = parser.parse_args()
    main(args)
