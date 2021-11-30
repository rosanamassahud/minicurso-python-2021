# # Manipulação de arrays Numpy

# ### Importando o NumPy
import numpy as np


# ### Alterando, adicionando e removendo elementos

# Criando um array de 1 dimensão
print('\nCriando um array de 1 dimensão\n')
a1D = np.random.randint(1,200, 12)
print(a1D)

# Criando um array de 2 dimensões
print('\nCriando um array de 2 dimensões\n')
a2D = np.random.randint(1,200, (3,4))
print(a2D)

# Criando um array de 3 dimensões
print('\nCriando um array de 3 dimensões\n')
a3D = np.random.randint(1,200, (2,3,6)) # 2 páginas/faces, 3 linhas, 6 colunas
print(a3D)

# Alterando o elemento do índice 0
a1D[0] = -1
print(a1D)

# Alterando o elemento da linha 1, coluna 2
a2D[1][2] = -1
print(a2D)

# Alterando o elemento da face 1, linha 2, coluna 4
a3D[1][2][4] = -1
print(a3D)

# Retorna array com elementos adicionados no final
a1D_modificado = np.append(a1D, [100, 130])
print(a1D_modificado)

print(a1D) # a1D não foi modificado

a2D_modificado = np.append(a2D, [100, 130]) # Lineariza a2D e insere os elementos no final
print(a2D_modificado)

print(a2D) # a2D não foi modificado

a3D_modificado = np.append(a3D, [100, 130]) # Lineariza a3D e insere os elementos no final
print(a3D_modificado)

print(a3D) # a3D não foi modificado

a1D_modificado2 = np.delete(a1D_modificado, [0, 1, 3])
print(a1D_modificado)
print(a1D_modificado2)


# ### Comparação entre arrays

a1D = np.array([1, 2, 3, 4, 5])
print(a1D)
b1D = np.array([3, 2, 1, 4, 5])
print(b1D)
print(a1D == b1D) # Comparação elemento a elemento

c1D = np.random.randint(1,10,20)
print(c1D)

print(c1D == 5)

print(c1D == 9)
print(c1D[c1D == 9])


# ### Operações entre arrays e escalares

a1D = np.arange(1,11)
print(a1D)

b1D = np.arange(1,20,2)
print(b1D)

c1D = 2 * a1D # Cada elemento de a1D será multiplicado por 2
print(c1D)

d1D = b1D + 5 # Soma 5 para cada elemento de b1D
print(d1D)

e1D = b1D - 3
print(e1D)

f1D = a1D / 5
print(f1D)

celsius = np.arange(-20, 36) # Cria um array com o valores de -20 a 35, representando a temperatura em graus Celsius
print(celsius)
fahrenheit = celsius * (9/5) + 32 # Cria um array convertendo cada valor em Celsius para fahrenheit
print(fahrenheit)

# Somando cada elemento de a1D a b1D
g1D = a1D + b1D
print(a1D)
print(b1D)
print("-"*31)
print(g1D)

# Outra forma de somar cada elemento de a1D a b1D
h1D = np.add(a1D, b1D)
print(a1D)
print(b1D)
print("-"*31)
print(h1D)

i1D = h1D - g1D
print(h1D)
print(g1D)
print("-"*31)
print(i1D)

# Outra forma de somar cada elemento de a1D a b1D
j1D = np.subtract(h1D, g1D)
print(h1D)
print(g1D)
print("-"*31)
print(j1D)

a1D = np.arange(1, 6)
print(a1D)

b1D = np.arange(6,11)
print(b1D)

c1D = a1D * b1D
print(c1D)

d1D = np.multiply(a1D, b1D)
print(d1D)

e1D = c1D / a1D
print(e1D)

f1D = np.divide(c1D, a1D)
print(f1D)

g1D = np.arange(1,10)
print(g1D)

raiz1D = np.sqrt(g1D)
print(raiz1D)


# ### Algumas funções
print("\nAlgumas funções")
d2D = np.random.randint(1, 101, (5,10)) # Array de 5 linhas x 10 colunas preenchidos com valores aleatórios entre 1 e 100
print(d2D)


# #### Obs: como os valores valores são gerados aleatoriamente, sua matriz provavelmente será diferente da gerada acima

# Soma de todos os elementos
print(d2D.sum())

# Soma de todos os elementos de cada coluna (eixo 0)
print(d2D.sum(axis = 0))

# Soma de todos os elementos de cada linha (eixo 1)
print(d2D.sum(axis = 1))


somacol = sum(d2D) # A função sum() do Python retornará a soma de todas as colunas
print(somacol)


# Retorna o menor valor geral
print(d2D.min())

# Retorna o menor valor de cada coluna (eixo 0)
print(d2D.min(axis=0))

# Retorna o menor valor de cada linha (eixo 1)
print(d2D.min(axis=1))

# Retorna o maior valor geral
print(d2D.max())

# Retorna o maior valor de cada coluna (eixo 0)
print(d2D.max(axis=0))


# Retorna o maior valor de cada linha (eixo 1)
print(d2D.max(axis=1))

# Retorna a soma cumulativa
print(d2D)
print(d2D.cumsum())

# Retorna a soma cumulativa para cada coluna (eixo = 0)
print(d2D.cumsum(axis = 0))

print(d2D)

# Retorna a soma cumulativa para cada linha (eixo = 1)
x = d2D.cumsum(axis = 1)
print(x)

# Retorna a média aritmética
print(d2D.mean())

# Retorna a média aritmética para cada coluna (eixo = 0)
print(d2D.mean(axis = 0))

# Retorna a média aritmética para cada linha (eixo = 1)
print(d2D.mean(axis = 1))

# Retorna o desvio padrão
print(d2D.std())

# Retorna o desvio padrão para cada coluna (eixo = 0)
print(d2D.std(axis = 0))

# Retorna o desvio padrão para cada linha (eixo = 1)
print(d2D.std(axis = 1))

print(d2D)

# Retorna a mediana (geral)
print(np.median(d2D))

# Retorna a mediana para cada coluna (eixo = 0)
print(np.median(d2D, axis = 0))

# Retorna a mediana para cada linha (eixo = 1)
print(np.median(d2D, axis = 1))


# ### Copiando e concatenando arrays
a2D = np.random.randint(1,50, (4,5))
print(a2D)


b2D = np.random.randint(50,100, (4,5))
print(b2D)

c2D = a2D
print(c2D)


# Aparentemente ocorreu uma cópia dos arrays, mas veja o que acontece se alterarmos alguns elementos
c2D[c2D < 20] = -1
print(c2D)


print(a2D)


# Os elementos de a2D também foram alterados. :-(

# Redefinindo os elementos de a2D
a2D = np.random.randint(1,50, (4,5))
print(a2D)


# Forma correta de copiar um array parece que com a forma de copiar uma lista
c2D = a2D.copy()
print(c2D)


c2D[c2D < 20] = -1
print(c2D)

print(a2D)

# Agora sim!!!

# ### Ordenando os elementos de um array

a1D = np.random.randint(1,100, 15)
print(a1D)

a1D.sort()
print(a1D)

a2D = np.random.randint(1,100, (6,10))
print(a2D)


a2D.sort() # Por padrão ordena o maior eixo (nesse caso o eixo 1, linhas)
print(a2D)

a2D.sort(axis=0) # Ordenando pelo eixo 0 (colunas)
print(a2D)

a2D = np.random.randint(1,100, (6,10))
print(a2D)

a2D.sort(axis=1) # Ordenando pelo eixo 1 (linhas)
print(a2D)

a2D = np.random.randint(1,100, (10,6))
print(a2D)

a2D.sort()
print(a2D)


# ### Transposição de arrays

a2D = np.array([[1,2,3,4],[5,6,7,8]])
print(a2D)


a2DT = a2D.T # Retorna a transposta
print(a2DT)


print(a2D) # a2D original não foi transposto

print(a2D.transpose()) # Retorna a transposta

print(a2D) # a2D original não foi transposto


# ### Mudando o formato de um array - reshape()

a1D = np.arange(1,25)
print(a1D)

print(a1D.shape)
a1D.shape = (2,12)
print(a1D.shape)
print(a1D)

a2D_4x6 = a1D.reshape(4,6)
print(a2D_4x6)

print(a1D)

a2D_3x8 = a1D.reshape(3,8)
print(a2D_3x8)


# ### Linearização de um array

x = a2D_3x8.flatten()
print(x)


y = a2D_3x8.ravel()
print(y)


# ### Combinando/concatenando arrays

a2D = np.random.randint(1,101,(3,9))
print(a2D)


b2D = np.random.randint(1,101,(5,9))
print(b2D)


c2D = np.random.randint(1,101,(5,4))
print(c2D)


# Concatenação de strings usa o operador "+"
str1 = "Python"
str2 = " & "
str3 = "Numpy"
str4 = str1 + str2 + str3
print(str4)

a2D = np.random.randint(1, 100, (6, 4))
print(a2D)
b2D = np.random.randint(1,100, (6,4))
print(b2D)

# O operador "+" aplicado a ndarrays não faz a concatenação, mas tentar somar elemento a elemento
print(a2D + b2D)

A = np.concatenate((a2D, b2D), axis = 0) # Concatenando pelo eixo das colunas (eixo 0) (empilhamento vertical)
print("a2D")
print(a2D)
print("")
print("b2D")
print(b2D)
print("")
print("Concatenação")
print(A)


B = np.vstack((a2D, b2D)) # Concatenando pelo eixo das colunas (eixo 0) (empilhamento vertical)
print("a2D")
print(a2D)
print("")
print("b2D")
print(b2D)
print("")
print("Concatenação")
print(B)


C = np.concatenate((a2D, b2D), axis = 1) # Concatenando pelo eixo das linhas (eixo 1) (empilhamento horizontal)
print("a2D")
print(a2D)
print("")
print("b2D")
print(b2D)
print("")
print("Concatenação")
print(C)


D = np.hstack((a2D, b2D)) # Concatenando pelo eixo das linhas (eixo 1) (empilhamento horizontal)
print("a2D")
print(a2D)
print("")
print("b2D")
print(b2D)
print("")
print("Concatenação")
print(D)


# ### Dividindo arrays

A_splitted = np.vsplit(A,3) # Divisáo vertical (corta no sentido das colunas)
print("Array original")
print(A)
print("")
print("1a parte")
print(A_splitted[0])
print("")
print("2a parte")
print(A_splitted[1])
print("")
print("3a parte")
print(A_splitted[2])

A_splitted3 = np.hsplit(A,2) # Divisão horizontal (corta no sentido das linhas)
print("Array original")
print(A)
print("")
print("1a parte")
print(A_splitted3[0])
print("")
print("2a parte")
print(A_splitted3[1])
print("")
