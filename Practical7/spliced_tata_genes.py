# import necessary modules
import os
import re

os.chdir('C:/Users/Administrator/Desktop/IBI/IBI/IBI1_2024-25/Practical7')

# input the one	of three possible splice donor/acceptor combinations
combination = input("Enter the splice donor and acceptor combinations from (GTAG, GCAG, ATAC): ")

# set the input and output path
input = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output = f'{combination}_spliced_genes.fa'

# repeat the last problem
genes = {}
with open(input, 'r') as file:
    for line in file:
        line = line.strip()
        if re.search(r'^>', line):
            gene_name = re.findall(r'gene:(\S+)', line)
            genes[gene_name[0]] = ''
        else:
            genes[gene_name[0]] += line

# find donor and accepter
keys_to_delete = []
for gene_name in genes:
    cut = combination[:2] + r'.*' + combination[2:]
    seqs = re.search(cut, genes[gene_name])
    if  not seqs:
        keys_to_delete.append(gene_name)

for key in keys_to_delete:
    del genes[key]

# repeat 
tata_genes = {}
for gene_name, sequence in genes.items():
    if re.search(r'TATA[AT]A[AT]', sequence):
        tata_genes[gene_name] = sequence

# output the result
with open(output, 'w') as file:
    for gene_name, sequence in tata_genes.items():
        t = re.findall(r'TATA[AT]A[AT]', sequence)
        file.write('>' + gene_name + ' :' + str(len(t)) + ' tata box' +'\n')
        file.write(sequence + '\n')

file.close()