import os

#Arquivos de texto simples

'''
1.   Abrir o arquivo
2.   Processar o arquivo
3.   Fechar o arquivo

Modos de abertura:
 - w: se o arquivo não existe, será criado. Se existe, trunca o arquivo
 - a: se o arquivo não existe, será criado. Se existe, adiciona a informação no final
 - r: se o arquivo não existe, retorna um erro

'''

f = open('arquivo.txt', 'w') 
f.write('Exemplo2 de arquivo de texto em Python\n')
f.close()

f = open('arquivo.txt', 'a')
f.write('Mais dados para o arquivo')
f.close()

f = open('arquivo.txt', 'r')
dados = f.read()
print(dados)
f.close()

def exclui_arquivo(arquivo):
    os.remove(arquivo)


exclui_arquivo('arquivo.txt')
