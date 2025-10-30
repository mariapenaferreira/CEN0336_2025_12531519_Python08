#!/usr/bin/env python3


import sys

# Verifica se o usuário passou o nome do arquivo.
if len(sys.argv) != 2:
    print("Uso: python3 Python08_7.py Python_08.fasta")
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

# Função para gerar o complemento reverso.
def rev_comp(seq):
    comp = {'A':'T','T':'A','C':'G','G':'C'}
    return "".join(comp.get(base, 'N') for base in reversed(seq))

# Função para traduzir uma sequência.
def traduzir(seq):
    aas = ""
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        if len(codon) == 3:
            aas += tabela_traducao.get(codon, "X")
    return aas

# Função para encontrar os ORFs dentro das sequências (trechos codificantes)
def encontrar_indices_orf(aa_seq):
    start = None
    for i, aa in enumerate(aa_seq):
        if aa == "M":
            start = i
            break
    if start is not None:
        for j in range(start, len(aa_seq)):
            if aa_seq[j] == "*":
                return start, j
    return None

# Leitura das sequências.
seqs = {}
with open(fasta_file, "r") as f:
    name = ""
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            name = line[1:]
            seqs[name] = ""
        else:
            seqs[name] += line.upper()

# Processamento dos 6 frames.
with open("Python_08.orf-longest.nt", "w") as out:
    for name, seq in seqs.items():
        rev_seq = rev_comp(seq)
        melhor_orf = ""
        for strand, s in [("forward", seq), ("reverse", rev_seq)]:
            for frame in range(3):
                frame_seq = s[frame:]
                aa_seq = traduzir(frame_seq)
                ids = encontrar_indices_orf(aa_seq)
                if ids:
                    start, stop = ids
                    # Converter o intervalo da tradução de aminoácidos (cada 1 aa = 3 nt)
                    orf_seq = frame_seq[start*3:(stop+1)*3]
                    if len(orf_seq) > len(melhor_orf):
                        melhor_orf = orf_seq
        out.write(f">{name}\n{melhor_orf}\n")

print("ORFs mais longas salvas em 'Python_08.orf-longest.nt'")
