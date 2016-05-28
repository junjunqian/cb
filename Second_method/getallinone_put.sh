#!/bin/bash
starcluster put mycluster /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/getallinone.sh /root
starcluster put mycluster /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/getallinone.py /root
starcluster put mycluster /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/result/0515output_name.csv /root
starcluster put mycluster /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/status.txt /root

for l in $(seq 9)
do 
    starcluster put mycluster --node node00$l /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/getallinone.py /root
done

for ((l=10; l <= 29 ; l++))
do
    starcluster put mycluster --node node0$l /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/getallinone.py /root
done
