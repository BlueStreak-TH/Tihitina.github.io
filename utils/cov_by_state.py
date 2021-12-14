import csv
import json

def convert_date_format(original):
    date, month, year = original.split('/')
    return year + '-' + month + '-' + date

def create_row_dict(row, cumulative_count):
    state = row[1]
    case = int(row[3])
    cumulative_count[state] = case

    return {
        "date": row[0],
        "name": state,
        "state": state,
        "value": cumulative_count[state]
        }

data = []
with open("data/raw/us-states.csv", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line = 0
    cumulative_count = {}
    for row in csv_reader:
        if line == 0:
            pass
        else:
            row_dict = create_row_dict(row, cumulative_count)
            data.append(row_dict)
            
        line += 1

with open('data/processed/covid_by_state.json', 'w') as f:
    json.dump(data, f)