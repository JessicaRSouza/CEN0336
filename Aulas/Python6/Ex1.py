#!/usr/bin/env python3

with open("Python_06.txt","r") as arquivo_leitura, open("Python_06_Maiúscula.txt","w") as arquivo_escri>        for linha in arquivo_leitura:
                #note a ausência de .rstrip(), visto que seria necessário recolocar o \n que ele tira
                linha = linha.upper() #Converte em maiúsculas
                arquivo_escrita.write(linha)
