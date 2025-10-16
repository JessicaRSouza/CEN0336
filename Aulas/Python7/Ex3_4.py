#!/usr/bin/env python3

import re

with open("Python_07.fasta", "r") as leitura:
	texto = leitura.read()

padrao = r"^>(\S+)\s*(.*)"

#Exercício 3
contador = 1
for correspondencia in re.finditer(padrao, texto, re.MULTILINE):
        print("Ocorrência {}: \nComeço: {} \nFim: {} \n".format(contador, correspondencia.start(), correspondencia.end()))
        contador+=1

#Exercício 4
for (id, desc) in re.findall(padrao, texto, re.MULTILINE):
	print("id: {} \tdesc: {}".format(id,desc))
