#!/usr/bin/env python3

#Exercício 6 - Obtenha um valor da linha de comando para "coisa_fav" e print o valor desse item do dici>
#Talvez você queira imprimir todas as chaves para o usuário, para que eles saibam o que escolher.
#Dê uma olhada em input().
favs = {
	"livro" : "A Hipótese do Amor",
	"som" : "Still Fell",
	"árvore" : "Ipê Branco",
	"organismo" : "Elefante"
	}

print("Escolha uma das opções:", list(favs.keys()))
coisa_fav = input("Digite sua escolha: ")
print("Sua escolha favorita é:", favs[coisa_fav])
