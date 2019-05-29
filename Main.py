import sys 
def readFasta(fasta):
    sequence = ''
    with open(fasta, 'r') as f: #open fasta, only read
        for line in f: #for line in fasta
            if line[0] == '>': #if first position of line is character '>'
                sequence += line #sequence is equal to line
    return sequence

sequence = readFasta(sys.argv[1])

print (sequence)
