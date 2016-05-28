#!/bin/bash
cd /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction

for ((l=0; l <= 29 ; l++))
do
    echo "This is some text" > /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/missedname/temp/$l/abc.txt
    echo "This is some text" > /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/smallname/temp/$l/abc.txt
    rm /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/missedname/temp/$l/*
    rm /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/smallname/temp/$l/*
done

# this is status file
rm -rf status.txt
starcluster get mycluster /root/status.txt /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction

# this is missedname file
starcluster get mycluster /root/missedname.txt /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/missedname/temp/0

for l in $(seq 9)
do 
    starcluster get mycluster --node node00$l /root/missedname.txt /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/missedname/temp/$l
done

for ((l=10; l <= 29 ; l++))
do
    starcluster get mycluster --node node0$l /root/missedname.txt /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/missedname/temp/$l
done

# this is smallname file
starcluster get mycluster /root/smallname.txt /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/smallname/temp/0

for l in $(seq 9)
do 
    starcluster get mycluster --node node00$l /root/smallname.txt /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/smallname/temp/$l
done

for ((l=10; l <= 29 ; l++))
do
    starcluster get mycluster --node node0$l /root/smallname.txt /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/smallname/temp/$l
done

# this is output file, has html code
starcluster get mycluster /root/0515* /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/htmlcode

for l in $(seq 9)
do 
    starcluster get mycluster --node node00$l /root/0515* /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/htmlcode
done

for ((l=10; l <= 29 ; l++))
do
    starcluster get mycluster --node node0$l /root/0515* /home/oski/Desktop/Shared/sf_stat_document/oceanwide/crunchbase/AWS/allfunction/htmlcode
done

python3 transfer.py
