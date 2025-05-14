from Bio.Align import substitution_matrices as sm
from Bio.Align import PairwiseAligner as pa

blosum62 = sm.load("BLOSUM62")
human_SODM = ''
mouse_SODM = ''
random = ''

with open('P04179.txt', 'r') as h:
    for line in h:
        if line.startswith('>'):
            continue
        seq = line.strip()
        human_SODM += seq

with open('P09671.txt', 'r') as m:
    for line in m:
        if line.startswith('>'):
            continue
        seq = line.strip()
        mouse_SODM += seq

with open('Random.txt', 'r') as r:
    for line in r:
        if line.startswith('>'):
            continue
        seq = line.strip()
        random += seq


#print(human_SODM)
#print(mouse_SODM)
#print(random)

def align_sequences(seq1, seq2):
    aligner = pa()
    aligner.substitution_matrix = blosum62
    alignment = next(aligner.align(seq1, seq2))
    print(alignment)

    score = alignment.score
    align_seq1 = alignment[0]
    align_seq2 = alignment[1]
    identical = sum(a == b for a, b in zip(align_seq1, align_seq2))
    percent_identity = identical / len(seq1) * 100

    return f'Score: {score}\nPercent Identity: {percent_identity:.2f}%\n' 

print(align_sequences(human_SODM, mouse_SODM))
print(align_sequences(human_SODM, random))
print(align_sequences(mouse_SODM, random))
print('Human SODM and mouse SODM are the most closely related.')