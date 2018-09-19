def readFasta(fasta):
    sequence = ''
    with open(fasta, 'r') as f:
        for line in f:
            if not line[0] == '>':
                sequence += line
            else:
                sequence += '\n'
    return sequence

sequence = readFasta('pdb_seq.fasta')

print (sequence)