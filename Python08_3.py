#!/usr/bin/env python3

import sys

# Verifica se o usuário passou o nome do arquivo.
if len(sys.argv) != 2:
    print("Uso: python3 Python08_3.py Python_08.fasta")
    sys.exit(1)

fasta_file = sys.argv[1]

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
with open("Python_08.codons-3frames.nt", "w") as out:
    for name, seq in seqs.items():
        for frame in range(3):
            codons = [seq[i:i+3] for i in range(frame, len(seq), 3) if len(seq[i:i+3]) == 3]
            out.write(f"{name}-frame-{frame+1}-codons\n")
            out.write(" ".join(codons) + "\n")

print("Arquivo 'Python_08.codons-3frames.nt' criado com sucesso!")
