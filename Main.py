import sys
def readFasta(fasta):
    sequence = ''
    with open(fasta, 'r') as f:
        for line in f:
            if line[0] == '>':
                sequence += line
    return sequence

sequence = readFasta(sys.argv[1])

print (sequence)