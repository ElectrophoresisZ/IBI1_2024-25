# import os
import os
# change the working directory to the directory where the script is located
print(os.getcwd())
os.chdir('C:/Users/Administrator/Desktop/IBI/IBI_practical_2025/Practical7')

# input: splice donor and acceptor combinations from (GTAG, GCAG, ATAC)
splice_sites = input('Enter the splice donor and acceptor combinations from (GTAG, GCAG, ATAC): ')
# output: a fasta file containing the spliced genes
open(f'{splice_sites}_spliced_genes.fa', 'w')

# import re
import re

# initialize variables
spliced_genes_dict = {}
spliced_gene = ''
donor = splice_sites[0:2]
acceptor = splice_sites[2:4]
tata_box_count = 0

# read the tata_genes.fa file and store the tata genes in a dictionary
with open('tata_genes.fa', 'r') as t:
    for line in t:
        # check if the line starts with '>'
        if line.startswith('>'):
            gene_name = line.strip().split()[0][1:]
            if spliced_gene:
                spliced_genes_dict[gene_name] = spliced_gene
            spliced_gene = ''
        else:
            spliced_gene += line.strip()
        

# iterate through the tata genes and check if they have the splice site combination
with open(f'{splice_sites}_spliced_genes.fa', 'a') as o:
    for gene_name, spliced_genes in spliced_genes_dict.items():
        if re.search(fr'{donor}.*?{acceptor}', spliced_genes.upper()):
            tata_box_count +=  len(re.findall(r'TATA[AT]A[AT]', spliced_genes.upper()))
            o.write(f'>{gene_name}\t{tata_box_count} tata box sites\n{spliced_genes}\n')
            tata_box_count = 0          
        else:
            o.write(f'>{gene_name}\n no splice site found\n')

t.close()
o.close()






'''
with open('S_gene.fa', 'r') as s:
    for line in s:
        if line.startswith('>'):
            gene_name = line.strip().split()[0][1:]
            if spliced_gene:
                spliced_genes_dict[gene_name] = spliced_gene
            spliced_gene = ''
        else:
            spliced_gene += line.strip()

with open(f'{splice_sites}_spliced_genes.fa', 'a') as o:
    for gene_name, spliced_genes in spliced_genes_dict.items():
        exons = re.split(fr'{donor}.*?{acceptor}', spliced_genes.upper())
        complete_exon_sequence = ''.join(exons)
        if re.search(r'TATA[AT]A[AT]', complete_exon_sequence):
            o.write(f'>{gene_name}\n{complete_exon_sequence}\n')
        else:
            o.write(f'>{gene_name}\n no tata box site found\n')
'''


        


        

        
