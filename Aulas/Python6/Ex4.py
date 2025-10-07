#!/usr/bin/env python3

linha_total = 0
carac_total = 0

with open("Python_06.fastq","r") as arq_fastq:
	for linha in arq_fastq:
		linha = linha.rstrip()
		linha_total += 1
		carac_total += len(linha)
	print("Número total de linhas: {}\nNúmero total de caracteres: {}\nComprimento médio da linha: {}".format(linha_total, carac_total, carac_total/linha_total))
