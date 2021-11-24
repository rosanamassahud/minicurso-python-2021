# # Verificando propriedades de um ndarray

# Importando o NumPy
import numpy as np


# Cria um ndarray com 10 elementos entre 0 e 9
a1D = np.random.randint(0, 10, 10)
print(a1D)


a2D = np.random.randint(1, 101, (4,5)) # Cria um ndarray de 4 linhas x 5 colunas com elementos entre 1 e 100
print(a2D)

a3D = np.random.random((3,4,5)) # Cria um ndarray de 3 páginas x 4 linhas x 5 colunas com elementos entre 0 e 1
print(a3D)


# ### Verificando o formato e quantidade de dimensões de um array - shape e dim

# A propriedade shape retorna o formato do array
print(a1D.shape)

print(a2D.shape)

print(a3D.shape)

# A propriedade ndim retorna o números de dimensões do array
print(a1D.ndim)

print(a2D.ndim)

print(a3D.ndim)


# ### Verificando o tamanho das dimensões de um array - len

print(len(a1D)) # Retorna o tamanho da 1a dimensão (quantidade de colunas)

print(len(a2D)) # Retorna o tamanho da 1a dimensão (quantidade de linhas)

print(len(a2D[0])) # Retorna o tamanho da 2a dimensão (quantidade de colunas)

print(len(a3D)) # Retorna o tamanho da 1a dimensão (quantidade de páginas)

print(len(a3D[0])) # Retorna o tamanho da 2a dimensão (quantidade de linhas)

print(len(a3D[0][0])) # Retorna o tamanho da 3a dimensão (quantidade de colunas)


# ### Verificando a quantidade de elementos de um array - size

print(a1D.size)

print(a2D.size)

print(a3D.size)


# ### Verificando o tipo dos elementos um array - dtype

print(a1D.dtype)

print(a1D.dtype.name)

print(a2D.dtype)

print(a2D.dtype.name)

print(a3D.dtype)

print(a3D.dtype.name)