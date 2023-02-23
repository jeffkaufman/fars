import os
import sys
import csv
import glob

st_case, year = sys.argv[1:]

for csv_fname in glob.glob("%s/*.CSV" % year):
    tidy_name = os.path.basename(csv_fname).replace(".CSV", "")
    cols = []
    st_case_col = None
    with open(csv_fname, errors='replace') as inf:
        for lineno, row in enumerate(csv.reader(inf)):
            if lineno == 0:
                if "ST_CASE" not in row:
                    break
                cols = row
                st_case_col = row.index("ST_CASE")
            elif row[st_case_col] == st_case:
                for colno, col in enumerate(row):
                    print("%s %s: %s" % (tidy_name, cols[colno], col))
