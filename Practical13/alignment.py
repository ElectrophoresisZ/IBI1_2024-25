# import the necessary module
from Bio.Align import substitution_matrices as sm

# read the blosum matrix
blosum62 = sm.load("BLOSUM62")
# initialize the sequences
human_SODM = ''
mouse_SODM = ''
random = ''

# read the files of sequences
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

# define a function to calculate the score of two sequences using a matrix
def calculate_score(seq1, seq2, matrix):
    score = 0
    for i in range(len(seq1)):
        score += matrix[seq1[i], seq2[i]]
    return score

# define a function to calculate the identity of two sequences
def calculate_identity(seq1, seq2):
    identity = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            identity += 1
    return f'{round(identity / len(seq1) * 100, 2)}%'

# print the results
print("Human SODM:", human_SODM)
print("Mouse SODM:", mouse_SODM)
print("Random:", random)

score1 = calculate_score(human_SODM, mouse_SODM, blosum62)
score2 = calculate_score(human_SODM, random, blosum62)
score3 = calculate_score(mouse_SODM, random, blosum62)

identity1 = calculate_identity(human_SODM, mouse_SODM)
identity2 = calculate_identity(human_SODM, random)
identity3 = calculate_identity(mouse_SODM, random)

print("Human-Mouse SODM Score:", score1)
print('Human-Mouse SODM Identity:', identity1)
print("Human-Random SODM Score:", score2)
print('Human-Random SODM Identity:', identity2)
print("Mouse-Random SODM Score:", score3)
print('Mouse-Random SODM Identity:', identity3)
print('Human SODM and mouse SODM are the most closely related.')