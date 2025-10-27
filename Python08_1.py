#!/usr/bin/env python3

#Recebe um arquivo multi-FASTA e calcula a composição de nucleotídeos
#(A, T, G, C) de cada sequência.

#Imprime no formato:
#seqNome    A_count    T_count    G_count    C_count

# Importa a biblioteca sys para ler o nome do arquivo da linha de comando.
import sys

# Verifica se o usuário realmente forneceu o arquivo FASTA como argumento.
if len(sys.argv) != 2:
    print("Uso: python3 Python08_1.py Python_08.fasta")
    sys.exit(1)

# Recebe o nome do arquivo FASTA.
fasta_file = sys.argv[1]

# Cria um dicionário que armazenará as informações:
# seqs[geneName][nucleotide] = count
seqs = {}

# Abre o arquivo FASTA.
with open(fasta_file, "r") as file:
    seq_name = ""
    seq = ""

    for line in file:
# Remove espaços e quebras de linhas.
        line = line.strip()
        if line.startswith(">"):
            # Se já temos uma sequência anterior, salva no dicionário.
            if seq_name:
                seqs[seq_name] = {
                    'A': seq.count('A'),
                    'T': seq.count('T'),
                    'G': seq.count('G'),
                    'C': seq.count('C')
                }
            seq_name = line[1:]
            seq = ""
        else:
            seq += line.upper()

    # Salva a última sequência.
    if seq_name:
        seqs[seq_name] = {
            'A': seq.count('A'),
            'T': seq.count('T'),
            'G': seq.count('G'),
            'C': seq.count('C')
        }

# Imprime os resultados no formato solicitado.
for gene in seqs:
    print(f"{gene}\tA:{seqs[gene]['A']}\tT:{seqs[gene]['T']}\tG:{seqs[gene]['G']}\tC:{seqs[gene]['C']}")
