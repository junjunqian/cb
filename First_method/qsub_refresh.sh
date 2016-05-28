#!/bin/bash 

#./qsub_refresh.sh "20160409_1740" "10" "2";

folder_num="$1"
sub_folder_num="$2"
sub2_folder_num="$3"
for l in $(seq ${sub2_folder_num})
do
    count=$((l-1));
    qsub refresh.sh "${folder_num}" "${sub_folder_num}" "`printf %03d $count`";
done
