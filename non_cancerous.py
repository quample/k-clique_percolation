import csv

ipfile = raw_input("enter input file: ")
ip = open (ipfile,'r')
ipreader = csv.reader(ip,delimiter='\n')
rank = list(ipreader)
ipfile1 = raw_input("enter input file: ")
ip1 = open (ipfile1,'r')
ipreader1 = csv.reader(ip1,delimiter='\n')
opfile = raw_input("name of file to be saved: ")
op = open (opfile,'w')
opwritter = csv.writer(op,delimiter='\t')
cancerous = list(ipreader1)
#print cancerous
#print rank
non_cancer = []
for i in rank:
    if i not in cancerous:
        non_cancer.append(i)
print non_cancer
for j in non_cancer:
    opwritter.writerow(j)
ip.close()
ip1.close()
op.close()
