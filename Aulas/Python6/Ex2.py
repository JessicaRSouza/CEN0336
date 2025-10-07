#!/usr/bin/env python3

with open("Python_06.txt","r") as arquivo_leitura, open("Python_06_Maiúscula.txt","w") as arquivo_escrita:
	for linha in arquivo_leitura:
		linha = linha.upper() #Converte em maiúsculas
		arquivo_escrita.write(linha)
