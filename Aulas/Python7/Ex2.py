#!/usr/bin/env python3

import re

with open("Python_07_nobody.txt", "r") as leitura, open("Jessica.txt", "w") as escrita:
	texto = leitura.read()
	novo_texto = re.sub(r"Nobody","Jessica", texto)
	escrita.write(novo_texto)
