# k-clique_percolation
python implementation of fast k-clique percolation

The FCPA.py is the actual Python implementation of the fast k-clique percolation algorithm.Accepts a network in the edgelist format. Outputs 2 types of files; 1 actual community files, where each new line corresponds to a new community of size atleast k. The second output file represents the details of each of the nodes in the community file. The program is designed to output these 2 files types recursively for k values 5 to 10.

The splitter-HPRD.py is a python script to convert the binary interactions from the HPRD database to that of an edgelist (ie format accepted by the FCPA algorithm)​

precission.py is a script to check the number of matching elements between 2 given lists. Accepts 2 files as input; 1 the obtained output file and next a file with true cancer entries to cross check with.

node_in_comm.py is a script to check how many genes in a given list are present in each of the communities. Aceepts 2 input files; first the community file and second the file containg list of genes to check.Can be used to check the cancerous genes present in wach communities and also the non-cancerous genes.

comm_analyzer.py is a program to check the hop distance metric of each gene entry. Takes 3 input files; first the network file in edge list format, second the list of genes to check hop distance from communities and third the community file. Output is a file showing the out of community gene and its shortest possible hop from any of the communities.

analysis.py is a python program to check the 4 centrality measures of the given graph. Accepts network in the edgelist format and outputs seperate ranked files based on each of induvidual centrality measures and also a Rank.csv file based on the combined values of each centrality measure of each of the genes.
