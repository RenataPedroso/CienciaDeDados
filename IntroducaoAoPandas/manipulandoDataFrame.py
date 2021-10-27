#importa a biblioteca pandas
import pandas as pd

#atribui um nome ao dataframe e relaciona ele ao arquivo que contém as informações da tabela
corona = pd.read_csv('http://emsapi.esy.es/datasets/corona_limpo.csv', sep=',')
alunosIndice = pd.read_excel('/content/indice_alunos.xlsx') #tirar o sep

#Mostra os 5 primeiros registros ou x primeiros registros
alunosIndice.head(60) 

#Mostra os 5 últimos registros da tabela ou x últimos registros
alunos.tail()

#utilizamos para mostrar quantas linhas e colunas temos no dataframe
corona.shape

#Apresenta quantidade de colunas quando com colchetes
alunos.shape[1]

#Mostra os tipos dos dados do dataframe
alunos.info()

#Apresenta os dados estastíticos do dataframe
alunos.describe()

#Cria um gráfico a partir dos dados numéricos do dataframe
alunos.plot()

#Para mostrar o maior valor da colunadodataframe
alunosIndice.max()

covid = pd.read_csv('/content/covid_19_data.csv', index_col=0)
covid.head(20)

#inspecionando o dataframe
type(covid)
covid.info()

#Apresenta o nome das colunas
covid.columns

