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

#Removendo linhas, colunas e atualizando o dataframe. Axis = 1 remove colunas, axis = 0 remove linhas
covid.drop(['Province/State'], axis=1,e inplace=True)
covid.head()

#Apresenta linhas que faltam valores, NA. Axis = 1 retorna colunas que faltam dados e axis = 0 retorna as linhas que faltam dados
covid.dropna(axis=0).head()

#Mostra por valores booleanos onde faltam valores no dataframe, onde false possui dados e true não possui dados
covid.isnull().head(50)

#Coloca uma mensagem ou número específico em dados faltantes
covid.fillna('Sem valor', inplace=True)
covid.head(50)

#Retorna uma coluna/Serie específica
covid['Country/Region']

#Retorna um dataframe da/s coluna/s selecionada/s
covid[['Country/Region']]
covid[['Country/Region', 'Confirmed']]

# retornando uma linha (observação) com base em um índice
covid.loc[10694]

# retornando uma linha (observação) com base em uma localização
covid.iloc[10694]


#Filtra e Retorna um DataFrame com casos confirmados acima de 80,000. 8e4 é 8 com 4 zeros = 80,000
covid[covid['Confirmed'] >8e4] 

#Filtra variáveis de forma qualitativa
covid[covid['Country/Region'] == 'Brazil']
covid[(covid['Confirmed'] > 8e4) & (covid['Recovered'] > 1e3)]


#Paramos em:

#Filtrando e Retornando um DataFrame com .loc
covid.loc[(covid['Confirmed'].between(8e4, 10e4, inclusive=False)) &
          (covid['Recovered'].between(12e3, 20e3, inclusive=True))]