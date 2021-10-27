#importa a biblioteca pandas
import pandas as pd

#atribui um nome ao dataframe e relaciona ele ao arquivo que contém as informações da tabela
corona = pd.read_csv('http://emsapi.esy.es/datasets/corona_limpo.csv', sep=',')
alunosIndice = pd.read_excel('/content/indice_alunos.xlsx') #tirar o sep