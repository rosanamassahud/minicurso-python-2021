"""
## Dados de arquivo csv
## Introdução ao pandas
"""
#pip install pandas

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv('oco.csv', sep="~")

#print(dados)
#print(dados.head())

#print(type(dados))

#print(dados.info())

#print(dados.dtypes)

#print(dados.describe())

#----------------------------------------------------------

#print(dados.ocorrencia_dia)

#print(dados.ocorrencia_dia.value_counts())

#print(dados.ocorrencia_dia.value_counts().head().to_frame('top 5'))

#----------------------------------------------------------
'''
grupo_estado = dados.groupby('ocorrencia_uf')
print(grupo_estado)

print(grupo_estado.describe())

plt.rc('figure', figsize=(20, 10))
plt.rcParams.update({'font.size': 30})
x = grupo_estado.ocorrencia_uf.value_counts()
fig = x.plot.bar(rot=90)
fig.set_xlabel('UF')
fig.set_ylabel('Ocorrências')
plt.show()
'''
#-----------------------------------------------------------
'''
grupo_classificacao = dados.groupby('ocorrencia_classificacao')
dfgc=pd.DataFrame(grupo_classificacao)
label_classificacao = dfgc[0]
fig = grupo_classificacao.ocorrencia_classificacao.value_counts().plot.pie(labels=label_classificacao, autopct='%.2f%%', shadow=True, startangle=90)
fig.set_ylabel('')
plt.show()
'''
#-----------------------------------------------------------
'''
print(label_classificacao)
fig = grupo_classificacao.ocorrencia_classificacao.value_counts().plot.bar()
fig.set_ylabel('Ocorrências')
fig.set_xlabel('Tipo da ocorrência')
fig.set_xticklabels(label_classificacao)
plt.show()
'''
#---------------------------------------------------------
#air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)
#print(air_quality.head())
#air_quality.plot()
#plt.show()
#----------------------------------------------------------

#air_quality["station_paris"].plot()
#plt.show()
#----------------------------------------------------------

#air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
#plt.show()
#----------------------------------------------------------

#air_quality.plot.box()
#plt.show()
#----------------------------------------------------------

#axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
#plt.show()