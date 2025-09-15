#!/usr/bin/env python3

ano = int(input("Digite um ano:"))

print ("Ano selecionado:", ano)

if ano % 4 == 0 and ano % 100 != 0:
	print ("O ano é bissexto")
else:
	print ("O ano não é bissexto")
