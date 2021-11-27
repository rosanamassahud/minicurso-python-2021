# # Indexação e fatiamento (slicing)

# Importando o NumPy
import numpy as np
import random

print('\n\nIndexação')
# Indexação

## A indexação de array é o mesmo que acessar um elemento de array.

## Podemos acessar um elemento de um array referindo-se ao seu número de índice.

## Os índices nos arrays NumPy começam com 0 (zero), o que significa que o primeiro elemento tem índice 0 (zero) e o segundo tem índice 1 (um) etc.

# Cria um ndarray com 10 elementos entre 0 e 9
a1D = np.random.randint(0, 10, 10)
print('Array de 1 dimensão: ', a1D)

a2D = np.random.randint(1, 101, (4,5)) # Cria um ndarray de 4 linhas x 5 colunas com elementos entre 1 e 100
print('Array de 2 dimensões:\n', a2D)

#a3D = np.random.random((3,4,5)) # Cria um ndarray de 3 páginas x 4 linhas x 5 colunas com elementos entre 0 e 1
a3D = np.random.randint(1,101, (3,4,5))
print('Array de 3 dimensões:\n', a3D)

#alt1 = np.random.uniform(1,101, 10)
#print(alt1)

# ### Acessando elementos específicos

# Acessando elementos de um ndarray de 1 dimensão
print('\nArray de 1 dimensão')
print(a1D)


# nome_do_array[índice]
print(a1D[0])

print(a1D[2])

print(a1D[-1]) # o índice -1 acessa o último elemento do array


indices = [3, 0, -1] # Definindo uma lista com os índices que se deseja acessar
print(a1D[indices])

print('\nArray de 2 dimensões')
# Acessando elementos de um ndarray de 2 dimensões
print(a2D)

# nome_da_matriz[linha][coluna]
print(a2D[1][2])


print(a2D[3][4])


indice_lin = [0, 1, 2, 3]
indice_col = [0, 1, 2, 3]

print(a2D[indice_lin, indice_col])


indice_lin = [0, 1, 2, 3]
indice_col = [3, 2, 1, 0]

print(a2D[indice_lin, indice_col])


indice_lin = [3, 2, 1, 0]
indice_col = [3, 2, 1, 0]

print(a2D[indice_lin, indice_col])

print()
print(a2D[:,[0,1,2,0]] )

print()
print(a2D[:,[0,1,2,0]][[1, 0, 1, 0]])


print(a2D)
print(a2D[[1, 0, 1, 0]][:,[0,1,2,0]] )

print('\nArray de 3 dimensões')
# Acessando elementos de um ndarray de 3 dimensões
print(a3D)


# nome_do_cubo[página][linha][coluna]
print(a3D[2][0][3])

print(a3D[0][3][1])

print('\n\nFatiamento (slicing)')
# ### Fatiamento (slicing)
# ### Fatiar em Python significa levar elementos de um determinado índice a outro índice

print('\nArray de 1 dimensão')
# Array de 1 dimensão
print(a1D)

a = a1D[1:5] # Índice 1 ao 4
print(a)


b = a1D[0:6] # Índice 0 ao 5
print(b)


c = a1D[:6] # Do início ao 5
print(c)


d = a1D[::2] # Do início ao fim, com passo 2
print(d)


e = a1D[-1::-1] # Do final até o início
print(e)

print('\nArray de 2 dimensões')
# Array de 2 dimensões
print(a2D)


linha0 = a2D[0] # Todos os elementos da linha 0 - outra forma seria: linha0 = a2D[0,:]
print(linha0)


linha1 = a2D[1,:] # Todos os elementos da linha 1
print(linha1)


linha2 = a2D[2,1:4] # Linha 2, colunas 1, 2 e 3
print(linha2)


linha3 = a2D[:][3] # a2D[:] retorna toda a matriz, então de toda a matriz queremos a linha 3 a2D[:][3]
linha3_ = a2D[3,:] # veja que dpa o mesmo resultado...
print(linha3)
print(linha3_)


coluna2 = a2D[:,2] # De todas as linhas, selecionar a coluna 2
print(coluna2)


coluna3 = a2D[1:,3] # Da linha um até a última, selecionar a coluna 3
print(coluna3)

print('\nArray de 3 dimensões')
# Array de 3 dimensões
print(a3D)

print('\n')
# Acessando a página/face 1
face1 = a3D[1]
print(face1)


# Acessando uma parte da face1
subface1 = a3D[1,0:3, 1:4] # da face 1, queremos, da linha 0 a 2, colunas de 1 até 3
print(subface1)


linha2face0 = a3D[0,2] # outra forma: linha2face0 = a3D[0,2,:]
print(linha2face0)


print(a3D)


linha1todasfaces = a3D[:,1] # outra forma: linha1todasfaces = a3D[:,1,:]
print(linha1todasfaces)


coluna3todasfaces = a3D[:,:,3]
print(coluna3todasfaces)


# ### Indexação com booleanos
print('---Indexação com booleanos')
a2D = np.random.randint(1, 501, (10, 8)) # Cria um ndarray de 10 linhas x 8 colunas com elementos entre 1 e 500
print(a2D)


a2D_250 = a2D >= 250
print('\n',a2D_250)


print('\n', a2D[a2D >= 250])


#mean() é a média dos números da coleção
print(a2D.mean())


print(a2D[a2D <= a2D.mean()])
