#!/usr/bin/env python3

#Exercício 1 - Escreva um script no qual você construa um dicionário de suas coisas favoritas
favs = {"livro" : "A Hipótese do Amor", "som" : "Still Fell", "árvore" : "Ipê Branco"}
print(favs)

#Exercício 2 - Print o seu livro favorito
print("Meu livro favorito é", favs["livro"])

#Exercício 3 - Print o seu livro favorito, mas use uma variável na chave
coisa_fav = "livro"
print("Minha coisa favorita é", favs[coisa_fav])

#Exercício 4 - Agora print sua árvore favorita
print("Minha árvore favorita é", favs["árvore"])

#Exercício 5 - Agora adicione o seu "organismo" favorito ao dicionário.
#Faça com que "organismo" seja o novo valor da chave "coisa_fav"

favs["organismo"] = "Elefante"
coisa_fav = "organismo"
print("Meu organismo favorito é", favs[coisa_fav])

#Exercício 7 - Altere o valor do seu organismo favorito
favs["organismo"] = "Sabiá"
print("Meu organismo favorito é", favs["organismo"])
