#!/bin/bash 

declare pycode=(["1"]="sele_bing.py" ["2"]="sele_google.py" ["3"]="sele_yahoo.py" ["4"]="yandex_ru.py")
cat choice_num.txt
for number in $(cat choice_num.txt)
do
    if [ $number -eq 4 ]
    then
        endnumber=$(($number - 3))
    else
        endnumber=$(($number + 1))
    fi
done

> choice_num.txt # delete all content in status.txt
echo $endnumber >> choice_num.txt
choicepy=${pycode["$number"]}
python "$choicepy" "$1" "$2"
python test1.py
rm html_file/00000.html

# python sele_yahoo.py https://www.crunchbase.com/organization/facebook#/entity real
# python sele_bing.py https://www.crunchbase.com/organization/facebook#/entity real
# python sele_google.py https://www.crunchbase.com/organization/facebook#/entity real
# python yandex_ru.py https://www.crunchbase.com/organization/facebook#/entity real
#python test1.py



#echo "TestScript2 Arguments received from TestScript1:"
#echo "$1"
#echo "$2"
#echo "$#"

