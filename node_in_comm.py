import csv

community = {}
prot_comm = {}
prot_comm_list = {}
known_cancer_prot=[]

ipfile1= raw_input("enter community file: ")
with open(ipfile1,"rb") as f2:
    reader2 = csv.reader(f2, delimiter=" ")
    for i, line in enumerate(reader2):
        community[i]=line

ipfile2= raw_input("enter the protein list file: ")
with open(ipfile2, "rb") as f1:
    reader1 = csv.reader(f1,delimiter="\t")
    for line in reader1:
        known_cancer_prot.extend(line)

for k, val in community.iteritems():
    for i in val:
        if i in known_cancer_prot:
            prot_comm_list.setdefault(i, []).append(k)

ipfile3 = raw_input("enter the file to save: ")
with open (ipfile3,"w") as q:
    wri= csv.writer(q,delimiter="\t")
    for k,v in prot_comm_list.items():
        wri.writerow((k,v))
