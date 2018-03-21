#!/usr/bin/python

from collections import defaultdict
import networkx as nx
import csv as csv

known_cancer_prot=[]
comm_cancer=[]
cancer_out_comm={}
community={}
lister=[]

print "---------------START---------------"

Ipfile = raw_input("enter input file: ")
print "Loading Graph."
G = nx.read_edgelist(Ipfile, nodetype=str, delimiter="\t")
print "Graph Loaded. "
ipfile1= raw_input("enter cancer list file: ")
ipfile2= raw_input("enter community file: ")

with open(ipfile2,"rb") as f2:
    reader2 = csv.reader(f2, delimiter=" ")
    for i, line in enumerate(reader2):
        community[i]=line

with open(ipfile1, "rb") as f1:
    reader1 = csv.reader(f1,delimiter="\t")
    for line in reader1:
        known_cancer_prot.extend(line)

for i in G:
    for val in community.values():
        if i in val:
            lister.append(i)        
    if ((i in known_cancer_prot) and (i not in lister)):
        cancer_out_comm[i]=int(9999)

for k in cancer_out_comm.keys():
    for i in community.values():
        for j in i:
            if nx.has_path(G,j,k):
                l=nx.shortest_path_length(G,j,k)
                if (l<cancer_out_comm[k]):
                    cancer_out_comm.update({k:int(l)})                                

with open ('comm_sp_length1.csv',"w") as q:
    wri= csv.writer(q,delimiter="\t")
    for k,v in cancer_out_comm.items():
        wri.writerow((k,v))
