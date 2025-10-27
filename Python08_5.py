#!/usr/bin/env python3

import sys

# Verifica se o usuário passou o nome do arquivo.
if len(sys.argv) != 2:
    print("Uso: python3 Python08_5.py Python_08.fasta")
    sys.exit(1)

fasta_file = sys.argv[1]

# Inserimos, por meio de um dicionário, a tabela que mostra o aminoácido correspondente à cada trinca de nucleotídeos.
tabela_traducao = {
    'GCT':'A','GCC':'A','GCA':'A','GCG':'A','CGT':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGA':'R','AGG':'R','AAT':'N','AAC':'N','GAT':'D','GAC':'D','TGT':'C','TGC':'C',
    'CAA':'Q','CAG':'Q','GAA':'E','GAG':'E','GGT':'G','GGC':'G','GGA':'G','GGG':'G',
    'CAT':'H','CAC':'H','ATT':'I','ATC':'I','ATA':'I','TTA':'L','TTG':'L','CTT':'L',
    'CTC':'L','CTA':'L','CTG':'L','AAA':'K','AAG':'K','ATG':'M','TTT':'F','TTC':'F',
    'CCT':'P','CCC':'P','CCA':'P','CCG':'P','TCT':'S','TCC':'S','TCA':'S','TCG':'S',
    'AGT':'S','AGC':'S','ACT':'T','ACC':'T','ACA':'T','ACG':'T','TGG':'W','TAT':'Y',
    'TAC':'Y','GTT':'V','GTC':'V','GTA':'V','GTG':'V','TAA':'*','TGA':'*','TAG':'*'
}

def rev_comp(seq):
    complement = {'A':'T','T':'A','C':'G','G':'C'}
    return "".join(complement.get(base,'N') for base in reversed(seq))

seqs = {}
with open(fasta_file,"r") as f:
    seq_name = ""
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            seq_name = line[1:]
            seqs[seq_name] = ""
        else:
            seqs[seq_name] += line.upper()

with open("Python_08.translated.aa", "w") as out:
    for name, seq in seqs.items():
        rev_seq = rev_comp(seq)
        for strand, s in [("forward", seq), ("reverse", rev_seq)]:
            for frame in range(3):
                codons = [s[i:i+3] for i in range(frame, len(s), 3) if len(s[i:i+3]) == 3]
                aa_seq = "".join([tabela_traducao.get(codon, 'X') for codon in codons])
                out.write(f">{name}-{strand}-frame-{frame+1}\n{aa_seq}\n")

print("Traduções gravadas em 'Python_08.translated.aa'.")
