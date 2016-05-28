#!/usr/bin/env python
try:
    fout=open("missedname/missedname_aa.txt","a")
    for num in range(0,30):
        f = open("missedname/temp/"+str(num)+"/"+"missedname.txt")
        for line in f:
            fout.write(line)
        f.close() # not really needed
    fout.close()
except:
	pass


fout=open("smallname/smallname_aa.txt","a")
for num in range(0,30):
    f = open("smallname/temp/"+str(num)+"/"+"smallname.txt")
    for line in f:
        fout.write(line)
    f.close() # not really needed
fout.close()

