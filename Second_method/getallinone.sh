#!/bin/bash
# smallfileaa to smallfilear, 5k per file
# status star with 0
declare -A animals=( ["1"]="aa" ["2"]="ab" ["3"]="ac" ["4"]="ad" ["5"]="ae" ["6"]="af" ["7"]="ag" ["8"]="ah" ["9"]="ai" ["10"]="aj" ["11"]="ak" ["12"]="al" ["13"]="am" ["14"]="an" ["15"]="ao" ["16"]="ap" ["17"]="aq" ["18"]="ar" ["19"]="as" ["20"]="at" ["21"]="au" ["22"]="av" ["23"]="aw" ["24"]="ax" ["25"]="ay" ["26"]="az")
cat status.txt
for number in $(cat status.txt)
    do endnumber=$(($number + 1))
done
> status.txt
echo $endnumber >> status.txt
letter=${animals["$endnumber"]}
split -l 500 0515output_name.csv smallfile
cat smallfile$letter | while IFS=, read -a csv_line
do
    echo "python3 allinone_get_csv.py ${csv_line[0]}" | qsub	
done 
rm -rf smallfile*