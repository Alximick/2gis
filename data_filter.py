#!/usr/local/bin/python3
import csv
import sys


def data_filter(filename):
    dct = {}
    import csv
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if row[0] not in dct:
                if row[2] == row[5]:
                    dct[row[0]] = [row[4], row[2]]
                else: 
                    dct[row[0]] = [row[1], row[2]]
            elif row[2] == row[5]:
                dct[row[0]] = [row[4], row[2]]
    with open('out.csv','w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows([["id", "name", "address", ""],])
        for row in dct:
            writer.writerows([[row, dct[row][0], dct[row][1],""],])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ./data_filter.py file')
        sys.exit(1)
    filename = sys.argv[1]
    data_filter(filename)
