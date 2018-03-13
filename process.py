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


if __name__ == '__main__':
    dt = process()
    fxt = get_fixture("Chelsea", "Man United", dt)

    print(fxt)
