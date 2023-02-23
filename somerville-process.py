#!/usr/bin/env python3

import glob
import csv
from collections import defaultdict

def start():
    for accident_csv in sorted(glob.glob("*/accident.csv")):
        year = accident_csv.split("/")[0]
        cols = {}

        def c(colname):
            if colname not in cols:
                return ''
            return row[cols[colname]]
        
        with open(accident_csv, errors="replace") as inf:
            for lineno, row in enumerate(csv.reader(inf)):
                if lineno == 0:
                    if "ST_CASE" not in row:
                        break
                    for colno, col in enumerate(row):
                        cols[col] = colno
                else:
                    if c('STATE') != '25': # MA
                        continue
                    if c('CITY') != '1190':  # SOMERVILLE
                        continue

                    print(
                        "%s-%s-%s %s fatals=%s peds=%s vehs=%s (%s and %s)" % (
                            year,
                            c('MONTH').zfill(2),
                            c('DAY').zfill(2),
                            c('ST_CASE'),
                            c('FATALS'),
                            c('PEDS'),
                            c('VE_TOTAL'),
                            c('TWAY_ID'),
                            c('TWAY_ID2')))

if __name__ == "__main__":
    start()
