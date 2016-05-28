#!/bin/bash
for i in 'MonteSereno' 'Woodside'
do
   echo "python3 getcompany_list.py 2005 2015 $i Califronia" | qsub
done 

