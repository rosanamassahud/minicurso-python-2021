#pip intall matplotlib

import matplotlib.pyplot as plt
import numpy as np

#-------------------------------------------------------------------
'''
Vamos criar um gráfico com a nossa planilha de vendas semestrais. 
Para isso, precisamos falar para o pyplot quais são os meses e 
quais são os valores de cada mês. Uma maneira de fazer isso é criar duas listas, 
uma com os meses e outra com os valores:
'''

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]

#Agora, basta falarmos para o pyplot plotar (plot) o nosso gráfico:
plt.plot(meses, valores)
#plt.bar(meses,valores)

#plt.ylim(100000, 120000)

#plt.title('Faturamento 1o semestre de 2021')
#plt.xlabel('Meses')
#plt.ylabel('Faturamento (R$)')

#E agora, mostrar o gráfico

plt.show()

#--------------------------------------------

#plt.plot([1, 2, 3, 4], [1, 4, 9, 16],'o')
#plt.axis([0, 6, 0, 20]) # [xmin, xmax, ymin, ymax]
#plt.show()

#----------------------------------------------
'''
x1=np.array([1,2,3,4,5,6,7,8,9,11])

x2 = x1
y2 = x1**2             # Numero elevado ao quadrado

x3 = x1
y3 = x1**3             # Numero elevado cubo

plt.plot(x1, y2 ,'g--', x2, y3, 'bs')

plt.show()
'''
#---------------------------------------------

#grupos = ['Produto A', 'Produto B', 'Produto C']
#valores = [1, 10, 100]
#plt.bar(grupos, valores)
#plt.show()

#--------------------------------------------
'''
# Define o stilo para ggplot
plt.style.use("ggplot")
#galeria de estilos do matplotlib: https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html

# Define as configurações dos plots
# Cada plot terá o mesmo tamanho de figuras (10,5)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))

# Dados para cada subplot
ax1.bar([1,2,3],[3,4,5]) #,color='#00BFFF'
ax2.barh([0.5,1,2.5],[0,1,2]) #, color='#00FF00'

ax1.set(title="Gráfico de Barras Verticais", xlabel="Eixo x", ylabel=" Eixo y")
ax2.set(title="Gráfico de Barras Horizontais", xlabel="Eixo x", ylabel="Eixo y")

plt.show()
'''

#----------------------------------------------
'''
# Quantidade de vendas para o Produto A
valores_produto_A = [6,7,8,4,4]

# Quantidade de vendas para o Produto B
valores_produto_B = [3,12,3,4.1,6]

# Cria eixo x para produto A e produto B com uma separação de 0.25 entre as barras
x1 =  np.arange(len(valores_produto_A))
x2 = [x + 0.25 for x in x1]

# Plota as barras
plt.bar(x1, valores_produto_A, width=0.25, label = 'Produto A', color = 'b')
plt.bar(x2, valores_produto_B, width=0.25, label = 'Produto B', color = 'y')

# coloca o nome dos meses como label do eixo x
meses = ['Agosto','Setembro','Outubro','Novembro','Dezembro']
plt.xticks([x + 0.25 for x in range(len(valores_produto_A))], meses)

# insere uma legenda no gráfico
plt.legend()

plt.title("Quantidade de Vendas")
plt.show()
'''

#------------------------------------------------------------
'''
grupos = ['Produto A', 'Produto B', 'Produto C']
valores = [1, 10, 100]
plt.barh(grupos, valores)
#plt.grid()
#plt.yticks(rotation=45)
plt.show()
'''
#-----------------------------------------------------------
'''
vendas = [3000, 2300, 1000, 500]
labels = ['E-commerce', 'Loja Física', 'e-mail', 'Marketplace']

# define o nível de separabilidade entre as partes, ordem do vetor representa as partes
#nivel_sep = (0.1, 0, 0, 0) 

plt.pie(vendas, labels=labels)

# define o formato de visualização com saída em 1.2%%, sombras e a separação entre as partes
#plt.pie(vendas, labels=labels, autopct='%1.2f%%', shadow=True, explode=nivel_sep)

#insere a legenda
plt.legend(labels)

# insere a legenda e a localização da legenda.
#plt.legend(labels, loc=2)

plt.show()
'''

#-----------------------------------------------------------------

'''
#Gera dados aleatórios com média em torno de 0 e desvio padrão em torno de 1
dados = np.random.normal(0, 1, size=500)

#Plota histograma com 10 bins:
plt.hist(dados, bins=10,color='g')

plt.show()
'''