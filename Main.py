import sys 
def readFasta(fasta):
    sequence = ''
    with open(fasta, 'r') as f: #abrimos fichero fasta, solo lectura
        for line in f: #para line dentro de fichero
            if line[0] == '>': #si la 1 posicion de line es >
                sequence += line <#sequence es igual a line(todos los que empiecen por >)
    return sequence# retorna sequence

sequence = readFasta(sys.argv[1])

print (sequence)
