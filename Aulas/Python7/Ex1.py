#!/usr/bin/env python3

import re

with open("Python_07_nobody.txt") as f:
	texto = f.read()

contador = 1
for correspondencia in re.finditer(r"Nobody", texto):
	print("Ocorrência {}: \nComeço: {} \nFim: {} \n".format(contador, correspondencia.start(), correspondencia.end()))
	contador+=1
