#!/usr/bin/env python3

numero = int(input("Digite um número:"))

if numero > 0:
	print ("O número é positivo")
	if numero < 50:
		print ("O número é menor que 50")
elif numero == 0:
	print ("O número é igual a zero")
else:
	print ("O número é negativo")
