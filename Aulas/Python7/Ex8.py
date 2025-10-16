#!/usr/bin/env python3

import re

with open("Python_07_ApoI.fasta", "r") as leitura:
	apoi = leitura.read()

padrao = r"([AG])(AATT[CT])"

apoi_corte = re.sub(padrao, r"\1^\2", apoi)

fragmentos = apoi_corte.split("^")
fragmentos = [f for f in fragmentos if not f.startswith(">")]

print(fragmentos)
