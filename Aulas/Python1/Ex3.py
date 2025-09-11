#!/usr/bin/env python3

import sys

nome = sys.argv[1]
cor = sys.argv[2]
atividade = sys.argv[3]
animal = sys.argv[4]

#O comando abaixo, embora utilize um só print(), faz com que a saída seja toda em uma mesma linha
print("Meu nome é:", nome, "Minha cor favorita é:", cor, "Minha atividade favorita é:", atividade, "Meu animal favorito é:", animal)

#Adicionando \n antes do texto da linha seguinte, dá uma quebra de linha e a saída é dividida
print("Meu nome é:", nome, "\nMinha cor favorita é:", cor, "\nMinha atividade favorita é:", atividade, "\nMeu animal favorito é:", animal)
