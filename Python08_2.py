#!/usr/bin/env python3

# Importa a biblioteca sys para ler o nome do arquivo da linha de comando.
import sys

# Verifica se o usuário passou o nome do arquivo.
if len(sys.argv) != 2:
    print("Uso: python3 Python08_2.py Python_08.fasta")
    sys.exit(1)

# Recebe o nome do arquivo FASTA.
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

# Cria o arquivo de saída e escreve os códons.
with open("Python_08.codons-frame-1.nt", "w") as out:
    for name, seq in seqs.items():
        codons = []
        # Cria grupos de 3 nucleotídeos (1º quadro de leitura, ou seja, começando do primeiro nucleotídeo).
        for i in range(0, len(seq), 3):
            codon = seq[i:i+3]
            if len(codon) == 3:  # ignora resto que não forma códon completo.
                codons.append(codon)
        out.write(f"{name}-frame-1-codons\n")
        out.write(" ".join(codons) + "\n\n")

print("Arquivo 'Python_08.codons-frame-1.nt' criado com sucesso!")
