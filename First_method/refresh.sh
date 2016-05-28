#!/bin/bash
sleep 30s

folder_num="$1"
sub_folder_num="$2"
sub2_folder_num="$3"
echo $folder_num
echo $sub_folder_num
echo $sub2_folder_num
echo aws s3 cp /root/result.csv s3://junstore/"${folder_num}"/"${sub_folder_num}"/"${sub2_folder_num}"/result.csv
echo aws s3 cp /root/done_url.csv s3://junstore/"${folder_num}"/"${sub_folder_num}"/"${sub2_folder_num}"/done_url.csv
aws s3 cp /root/result.csv s3://junstore/"${folder_num}"/"${sub_folder_num}"/"${sub2_folder_num}"/result.csv
aws s3 cp /root/done_url.csv s3://junstore/"${folder_num}"/"${sub_folder_num}"/"${sub2_folder_num}"/done_url.csv
rm comp_html.sh.e*
rm comp_html.sh.o*
rm done_url.csv
rm html_file/*.html
python2.7 refresh.py
#folder_num=20160409_1740
#sub_folder_num=10
#sub2_folder_num=000
#echo aws s3 cp /root/result.csv s3://storecb/"${folder_num}"/"${sub_folder_num}"/"${sub2_folder_num}"/result.csv
