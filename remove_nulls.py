#!/usr/bin/env python3

import sys

year, = sys.argv[1:]
person_csv = "%s/person.csv" % year

with open(person_csv, encoding='latin1') as inf:
    f = inf.read()
with open(person_csv, 'w') as outf:
    outf.write(f.replace("\0", " "))
