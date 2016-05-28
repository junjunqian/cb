#!/bin/bash 

while IFS=, read -a csv_line
do
    qsub comp_html.sh "${csv_line[0]}" "${csv_line[2]}"
done < raw.csv

#echo "TestScript1 Arguments:"
#echo "$1"
#echo "$2"
#echo "$#"
#./testscript2.sh "$1" "$2"   # keep use this one

# run
# ./testscript1 "Firstname Lastname" testmail@domain.com
# ./testscript1.sh https://www.crunchbase.com/organization/facebook#/entity real
