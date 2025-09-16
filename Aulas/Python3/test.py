#!usr/bin/env python3

dna = "TGAACATCTAAAAGATGAAGTTT"
dna_len = len(dna)
gene_name = "Brca1"

descricao_gene = "Esta sequência: {} possui {} nucleotídeos e é encontrada em {}."

print(descricao_gene.format(dna, dna_len, gene_name))
