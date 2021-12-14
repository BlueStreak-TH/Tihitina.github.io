import csv
import json

def convert_date_format(original):
    date, month, year = original.split('/')
    return year + '-' + month + '-' + date

def create_row_dict(row, cumulative_count):
    county = row[1]
    state = row[2]
    try:
        case = int(row[4])
    except ValueError: 
        print("value error")
        print(row)
        case = 0
    if state not in cumulative_count:
        cumulative_count[state] = {}
        cumulative_count[state][county] = 0

    cumulative_count[state][county] = case

    return {
        "date": row[0],
        "name": county,
        "county": county,
        "state": state,
        "value": cumulative_count[state][county]
        }

final_data = dict()
with open("data/raw/us-counties.csv", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line = 0
    cumulative_count = {}
    for row in csv_reader:
        if line == 0:
            pass
        else:
            county = row[1]
            state = row[2]
            try:
                case = int(row[3])
            except ValueError:
                case = 0
            if state not in final_data:
                final_data[state] = []
            
            row_dict = create_row_dict(row, cumulative_count)

            final_data[state].append(row_dict)
            
        line += 1

for state in final_data:
    # try:
    #     with open(f"data/processed/{state}"):
    #         pass
    # except FileNotFoundError:
    #     import os
    #     os.mkdir(f"data/processed/{state}")
    # for county in final_data[state]:
    with open(f'data/processed/cov_by_county_{state}.json', 'w+') as f:
        json.dump(final_data[state], f)