#!/usr/bin/env python3

import re

corte_enzimas = {}
with open("bionet.txt", "r") as enzima_read, open("dict_enzimas", "w") as enzima_write:
	for intervalo in range(10):
		next(enzima_read)

	for linha in enzima_read:
		linha = linha.strip()
		if not linha:
			continue

		colunas = linha.split()
		enzima = colunas[0]
		padrao = colunas[1]

		corte_enzimas[enzima] = padrao
