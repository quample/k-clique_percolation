#!/usr/bin/python

import csv
ipfile_act = raw_input("enter actual file: ")
ip1 = open (ipfile_act,'r')
ipfile_pred = raw_input("enter predicted file: ")
ip2 = open (ipfile_pred,'r')
ipreader_act = csv.reader(ip1,delimiter='\n')
ipreader_pred = csv.reader(ip2,delimiter='\n')
c = 0
y_actual = []
y_predi = []
out=[]
#n=int(raw_input("enter the cut-off: "))
for i in ipreader_act:
    y_actual.append(i)
top500=y_actual
for j in ipreader_pred:
    y_predi.append(j)

for i in top500:
    #print i
    for j in y_predi:
        #print j
        if i==j:
            c=c+1
            out.append(i)
print c
handle, extension = ipfile_act.split(".")
opf='precision_'+handle+'.csv'
writer = csv.writer(open(opf,'w'), delimiter = '\t')
for k in out:
    writer.writerow(k)
