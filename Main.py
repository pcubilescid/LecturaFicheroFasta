def readFasta(fasta):
    sequence = ''
    with open(fasta, 'r') as f:
        for line in f:
            if line[0] == '>':
                sequence += line
    return sequence

sequence = readFasta('pdb_seq.fasta')

print (sequence)