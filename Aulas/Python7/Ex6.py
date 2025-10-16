#!/usr/bin/env python3

import re

with open("Python_07_ApoI.fasta", "r") as leitura:
	texto = leitura.read()

padrao = r"[AG]AATT[CT]"

contador = 1
for correspondencia in re.finditer(padrao, texto, re.MULTILINE):
        print("Ocorrência {}: \nSequência: {} \nComeço: {} \nFim: {} \n".format(contador, correspondencia.group(), correspondencia.start(), correspondencia.end()))
        contador+=1

