#!/usr/bin/env python3

#Obtenha "coisa_fav" da linha de comando e um novo valor para essa chave.
#Altere o valor com o valor inserido pelo usuário.

favs = {
    "livro": "A Hipótese do Amor",
    "som": "Still Fell",
    "árvore": "Ipê Branco",
    "organismo": "Sabiá"
}

print("Escolha uma das opções:", list(favs.keys()))

coisa_fav = input("Digite sua escolha: ")

favs[coisa_fav] = input("Digite o novo valor para a chave:")

print("Atualização: \nChave: {} \nNovo valor: {} \nLista completa: {}".format(coisa_fav, favs[coisa_fav], favs))
