#!/usr/bin/env python3

with open("Python_06.seq.txt","r") as seq_original:
	for linha in seq_original:
		linha = linha.rstrip()
		id_gene, seq = linha.split("\t")
		seq_complemento = seq.replace("A","t").replace("T","a").replace("G","c").replace("C","g")
		seq_complemento = seq_complemento.upper()
		seq_comp_rev = seq_complemento[::-1]
		print(">{}\n{}".format(id_gene, seq_comp_rev))
