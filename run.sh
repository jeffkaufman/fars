#!/bin/bash

for year in $(seq 1975 2020) ; do
    if [ ! -d $year ]; then
        wget https://static.nhtsa.gov/nhtsa/downloads/FARS/${year}/National/FARS${year}NationalCSV.zip
        unzip -d $year FARS${year}NationalCSV.zip
        ./remove_nulls.py $year
    fi
done

./halloween-process.py
