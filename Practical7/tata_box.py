# import os
import os
# change the working directory to the directory where the script is located
print(os.getcwd())
os.chdir('C:/Users/Administrator/Desktop/IBI/IBI_practical_2025/Practical7')

# import re
import re

# create a new file to store the TATA box genes
tata_genes = open('tata_genes.fa', 'a')

# initialize a dictionary to store the S gene sequences
S_gene_dict = {}
gene = ''

# read the S gene file and store the sequences in a dictionary
with open('S_gene.fa', "r") as f:
    for line in f:
        if re.search(r'>', line):
            gene_name = line.strip().split()[0][1:]
            if gene:
                S_gene_dict[previous_gene_name] = gene          
            previous_gene_name = gene_name
            gene = ''
        else:
            gene += line.strip()
        if gene:
            S_gene_dict[previous_gene_name] = gene

# iterate through the S gene dictionary and write the TATA box genes to a new file
for gene_name, gene in S_gene_dict.items():
    if re.search(r'TATA[AT]A[AT]', gene):
        tata_genes.write('>'+ gene_name + '\n')
        for i in range(0, len(gene), 60):
            tata_genes.write(gene[i:i+60] +'\n')

# close the file
tata_genes.close()