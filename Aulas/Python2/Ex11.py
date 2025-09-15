#!/usr/bin/env python3

numero = int(input("Digite um número:"))

if numero > 0:
	print ("O número é positivo")
	if numero < 50:
		if numero % 2 == 0:
			print ("O número é par e menor que 50")
	else:
		if numero % 3 == 0:
			print ("O número é maior que 50 e divisível por 3")
elif numero == 0:
	print ("O número é igual a zero")
else:
	print ("O número é negativo")
