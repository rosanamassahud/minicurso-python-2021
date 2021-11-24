# pip install numpy

# Importando o NumPy
import numpy as np

#verifica a versão instalada do numpy
print(np.__version__)

#Criando arrays de 1 dimensão
a1D = np.array([1, 2, 3, 4, 5])

print(a1D)

# O objeto criado é do tipo ndarray (n-dimensional array)
print(type(a1D))

# Verificando o tipo dos elementos
print(a1D.dtype)

# Construindo um outro objeto ndarray, espcificando o tipo dos dados
b1D = np.array([1, 2, 3], dtype = float)
print(b1D)

print(b1D.dtype)

c1D = np.array([1,2,3], dtype = str)
print(c1D)

print(c1D.dtype)

# str > float > int > bool
d1D = np.array([1, 3.14, "NumPy", True])
print(d1D)

print(d1D.dtype)

e1D =  np.array([2, 3.14, False, True])
print(e1D)

print(e1D.dtype)


f1D = np.array([1, False, True])
print(f1D)

print(f1D.dtype)

g1D = np.array([False, True])
print(g1D)

print(g1D.dtype)

#Criando arrays de 2 dimensões

a2D = np.array([ [1,2,3], [4,5,6], [7,8,9] ])
print(a2D)

a2D.dtype

#Criando arrays de 3 dimensões

## A terceira dimensão é chamada de 'página' ou 'face'

a3D = np.array( [ [ [1,2,3], [4,5,6], [7,8,9] ], [ [11,12,13], [14,15,16], [17,18,19] ], [ [21,22,23], [24,25,26], [27,28,29] ]] )
print(a3D)

print(a3D.dtype)

# Outras formas de criar arrays

## Arrays preenchidos com zeros - zeros()

# 1 dimensão, default é float

azeros = np.zeros(5)
print(azeros)

print(azeros.dtype)

# 1 dimensão, especificando o tipo
azeros = np.zeros(5, dtype=int)
print(azeros)

print(azeros.dtype)

# 2 dimensões
bzeros = np.zeros((3, 4)) # 3 linhas e 4 colunas
print(bzeros)

# 3 dimensões
czeros = np.zeros((3, 4, 2)) # 3 páginas, 4 linhas e 2 colunas
print(czeros)

# ### Arrays preenchidos com 1's - ones()

# 1 dimensão
a_um_1D = np.ones(5)
print(a_um_1D)

b_um_1D = np.ones(10, dtype = str)
print(b_um_1D)


c_um_1D = np.ones(5, dtype = int)
print(c_um_1D)

# 2 dimensões
d_um_2D = np.ones((4, 3)) # 4 linhas e 3 colunas
print(d_um_2D)

# 3 dimensões
e_um_3D = np.ones((5, 2, 3)) 
print(e_um_3D)


# 4 dimensões
# a quarta dimensão pode ser entendida como uma matriz de cubos
# 3 cubos, onde cada cubo contem 4 faces, cada face possui 2 linhas e 3 colunas
f_um_4D = np.ones((3, 4, 2, 3)) 
print(f_um_4D)


# ### Arrays preenchidos com faixas de valores - arange()

# Cria um ndarray preenchido com  os elementos de 0 a n-1
# No exemplo abaixo vai criar um ndarray com os elementos 0 a 9
a1D = np.arange(10)
print(a1D)


# Cria um ndarray preenchido com os elementos variando entre o valor inicial e o valor final - 1
# Nesse exemplo vai criar um array com os elementos de 5 a 14
b1D = np.arange(5, 15)
print(b1D)

# Cria um ndarray preenchido com os elementos variando entre o valor inicial e o valor final - 1, com um determinado step
# No exemplo vai criar um array com os elementos de 5 a 100, com passo 10. Ou seja: 5, 15, 25...95
c1D = np.arange(5,100, 10)
print(c1D)


# ### Criando arrays preenchidos com valores igualmente espaçados - linspace()

# Cria um array com n elementos entre o valor inicial e valor final, igualmente espaçados
d1D = np.linspace(0,10, 2) # Cria um array com 2 valores entre 0 e 10
print(d1D)

e1D = np.linspace(0,10, 4) # Cria um array com 4 valores entre 0 e 10
print(e1D)


f1D = np.linspace(1,1000) # Se não for passada a quantidade de elementos, o padrão é gerar 50 elementos
print(f1D)

g1D = np.linspace(1,1000, dtype = int) # gerando int, a função simplesmente corta as casas decimais
print(g1D)

h1D = np.linspace(0,50, 10, endpoint = True) # O valor final é incluído
print(h1D)


i1D = np.linspace(0,50, 10, endpoint = False) # O valor final não é incluído
print(i1D)


# ### Criando arrays preenchidos com um único valor passado por parâmetro - full()

a1D = np.full(10, 5) # ndarray contendo 10 números 5
print(a1D)

a2D = np.full((3, 5), 4)  # ndarray de 3 linhas e 5 colunas contendo o número 4
print(a2D)

a3D = np.full((3, 5, 8), -1)  # ndarray de 3 páginas, 5 linhas e 8 colunas contendo o número -1
print(a3D)


# ### Criando matriz identidade - eye()

ident = np.eye(5) # Cria uma matriz 5x5 preenchida com 1s na diagonal principal e 0 nas posições restantes
print(ident)


# ### Criando matriz com elementos aleatórios

a1D = np.random.randint(0, 100, 10) # Cria um ndarray com 10 elementos entre 0 e 99
print(a1D)


a2D = np.random.randint(1, 500, (4,5))
print(a2D)


# Gerando 10 combinações para a mega-sena
# Valores vão de 1 a 60, 10 páginas, 1 linha, 6 colunas
a3D = np.random.randint(1,61,(10,1,6)) 
print(a3D)


b1D = np.random.random(10) # Cria um ndarray contendo 10 elementos aleatórios entre 0 e 1
print(b1D)

c2D = np.random.random((4,5)) # Cria um ndarray de 4 linhas e 5 colunas contendo elementos aleatórios entre 0 e 1
print(c2D)
