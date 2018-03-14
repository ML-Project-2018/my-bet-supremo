#!/usr/bin/python3
import csv

import pandas as pd
import numpy as np


def process():
    data = []
    for i in range(1, 27):
        with open('data/E0 ({}).csv'.format(i), mode='rt', encoding='utf-16') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row[:26])

    return pd.DataFrame(np.array(data))


def get_fixture(home_team, away_team, data):
    fixture = []
    x = 0
    size = 10

    for i in range(data.shape[0]):
        d = data[x:size]
        for index, row in d.iterrows():
            if (row[2] == home_team or row[3] == away_team) and (
                    row[2] == away_team or row[3] == home_team):
                fixture.append(row)

        x += 10
        size += 10

    return pd.DataFrame(fixture)


def get_data():
    data = []
    with open('data/E0 (20).csv', 'r', encoding='utf-16') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row[: 26])

    return pd.DataFrame(np.array(data))

def trail(data, team_name):
    fixtures = []

    x = 0
    size = 10

    for i in range(data.shape[0]):
        d = data[x:size]
        for index, row in d.iterrows():
            record = np.empty(9, dtype=object)

            if row[2] == team_name or row[3] == team_name:
                row = row.tolist()
                record[0] = row[1].split('/')[1]

                if row[2] == team_name:
                    record[1] = 1
                    if row[9] == 'A': record[4] = 0
                    elif row[9] == 'H': record[4] = 3
                    else: record[4] = 1

                elif row[3] == team_name:
                    record[1] = 0
                    if row[9] == 'A': record[4] = 3
                    elif row[9] == 'H': record[4] = 0
                    else: record[4] = 1

                record[2] = row[7]
                record[3] = row[8]
                record[5] = row[23]
                record[6] = row[24]
                record[7] = row[25]
                record[8] = row[4]

                fixtures.append(record)

        x += 10
        size += 10

    return pd.DataFrame(fixtures)


if __name__ == '__main__':
    dt = process()
    fxt = get_fixture("Chelsea", "Man United", dt)

    print(fxt)
