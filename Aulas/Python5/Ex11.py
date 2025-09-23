#!/usr/bin/env python3

#Exercício 11 - Escreva um script paraa encontrar a interseção, diferença, união e diferença simétrica.

SetA = {"3", "14", "15", "9", "26", "5", "35", "9"}
SetB = {"60", "22", "14", "0", "9"}

print("Conjunto A: ", SetA)
print("Conjunto B: ", SetB)

#Interseção
print("Interseção: ", SetA & SetB)

#Diferença
print("Diferença: ", SetA - SetB)

#União
print("União: ", SetA | SetB)

#Diferença Simétrica
print("Diferença Simétrica: ", SetA ^ SetB)
