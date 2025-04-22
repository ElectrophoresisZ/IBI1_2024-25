# import re
import re

# define sequence
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

# define pattern to match introns
pattern = re.compile(r'GT.*AG')
matches = pattern.finditer(seq)

# initialize largest intron
largest_intron = ''
# iterate through all introns and find the largest one
for match in matches:
    intron = match.group()
    if len(intron) > len(largest_intron):
        largest_intron = intron

# print the largest intron and its length
print(largest_intron)
print(len(largest_intron))
