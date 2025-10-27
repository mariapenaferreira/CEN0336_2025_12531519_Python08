#!/usr/bin/env python3

import sys

# Verifica se o usuário passou o nome do arquivo.
if len(sys.argv) != 2:
    print("Uso: python3 Python08_4.py Python_08.fasta")
    sys.exit(1)

fasta_file = sys.argv[1]

# Função para obter o complemento reverso.
def rev_comp(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(complement.get(base, 'N') for base in reversed(seq))

# Lê o arquivo FASTA e armazena as sequências.
seqs = {}
with open(fasta_file, "r") as f:
    seq_name = ""
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            seq_name = line[1:]  #remove o ">"
            seqs[seq_name] = ""
        else:
            seqs[seq_name] += line.upper()  #concatena as linhas da sequência.

# Cria o arquivo de saída e escreve os códons
with open("Python_08.codons-6frames.nt", "w") as out:
    for name, seq in seqs.items():
        rev_seq = rev_comp(seq)
        for strand, s in [("forward", seq), ("reverse", rev_seq)]:
            for frame in range(3):
                codons = [s[i:i+3] for i in range(frame, len(s), 3) if len(s[i:i+3]) == 3]
                out.write(f"{name}-{strand}-frame-{frame+1}\n")
                out.write(" ".join(codons) + "\n")

print("Códons dos 6 quadros gravados em 'Python_08.codons-6frames.nt'.")
