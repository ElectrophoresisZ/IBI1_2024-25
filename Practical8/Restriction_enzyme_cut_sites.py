# define a function to find restriction enzyme cut sites in a DNA sequence
def restriction_enzyme_cut_sites(DNA_seq, enzyme_restriction_site):
    # import re
    import re
    # initialize an empty list to store the restriction site positions
    site_list = []
    # use re.search() to find the restriction site in the DNA sequence
    if re.search(enzyme_restriction_site, DNA_seq):
        for i in range(len(DNA_seq)):
            frac = DNA_seq[i:i+len(enzyme_restriction_site)]
            # check if the current substring matches the restriction site
            if frac == enzyme_restriction_site:
                site_list.append(f'position{i+1}')
        return 'Restriction sites are found at '+ ', '.join(site_list) + '.'
    # if no restriction site is found, return a message
    else:
        return "No restriction site found!"
    
# Example usage:
print(restriction_enzyme_cut_sites('ATCGATCGATCGTACG', 'ATCG'))
print(restriction_enzyme_cut_sites('ATCGATCGATCGTACG', 'CGAT'))