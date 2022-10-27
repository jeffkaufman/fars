#!/usr/bin/env python3

import glob
import csv
from collections import defaultdict

def bucket_age(age):
    if age >= 75: return "75+"
    if age >= 50: return "50-74"
    if age >= 35: return "35-49"
    if age >= 25: return "25-34"
    if age >= 20: return "20-24"
    if age >= 15: return "15-19"
    if age >= 10: return "10-14"
    if age >= 6: return "6-9"
    if age >= 3: return "3-5"
    return "0-2"

def start():
    fatalities = defaultdict(int) 
    fatalities_oct31 = defaultdict(int) 
    fatalities_apr30 = defaultdict(int) 

    apr30_by_year = defaultdict(int)
    
    daily_child_fatalities = defaultdict(int)
    
    for person_csv in sorted(glob.glob("*/person.csv")):
        year = person_csv.split("/")[0]

        # bad data
        if year < "1982": continue

        if False and (year < "1990" or year > "2010"):
            continue # replicate the chart
        
        with open(person_csv) as inf:
            for lineno, row in enumerate(csv.reader(inf)):
                if lineno == 0:
                    i_per_typ = row.index("PER_TYP")
                    i_month = row.index("MONTH")
                    i_day = row.index("DAY")
                    i_age = row.index("AGE")
                else:
                    per_typ = row[i_per_typ]

                    if per_typ != "5":
                        continue
                    
                    month = int(row[i_month])
                    day = int(row[i_day])
                    age = int(row[i_age])

                    if month == 99: continue
                    if day == 99: continue
                    if age > 900: continue

                    #if age <= 18:
                    if 1 < age < 11:
                        daily_child_fatalities[month, day] += 1
                    
                    age = bucket_age(age)

                    fatalities[age] += 1
                    if month == 10 and day == 31:
                        fatalities_oct31[age] += 1
                    if month == 4 and day == 30:
                        fatalities_apr30[age] += 1
                        if age == "6-9":
                            apr30_by_year[year] += 1
                            #if year == "1992":
                            #    print (row)
                    


    if True:
        print("<tr><th>Age<th>N<th>Relative Risk")
        for bucket in sorted(fatalities):
            print("<tr><td>%s<td>%s<td>%.1fx" % (
                bucket,
                fatalities_oct31[bucket],
                fatalities_oct31[bucket]/fatalities[bucket]*365.25))
        print()

        print("<tr><th>Age<th>N<th>Relative Risk")
        for bucket in sorted(fatalities):
            print("<tr><td>%s<td>%s<td>%.1fx" % (
                bucket,
                fatalities_apr30[bucket],
                fatalities_apr30[bucket]/fatalities[bucket]*365.25))
        print()
    elif False:
        for year, deaths in sorted(apr30_by_year.items()):
            print(year, deaths)
    elif True:
        for (month, day), deaths in sorted(daily_child_fatalities.items()):
            print("%s-%s\t%s" % (
                str(month).zfill(2), str(day).zfill(2), deaths))


if __name__ == "__main__":
    start()
