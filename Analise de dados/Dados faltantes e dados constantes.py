import numpy as np #como importar o numpy

import pandas as pd #como importar o pandas 

nomedodataframe = pd.read_csv('nomedapasta')

nomedodataframe.head(10)# parametros para ver 10 primeiras linhas 

nomedodataframe['coluna'].value_counts()#Para analisar a frequencia dos dados dessa coluna 

nomedodataframe.info()#Paraa analisar as informaçoes se a coluna acima é relevante ou se é onstante 

nomedodataframe = nomedodataframe.drop(columns=['coluna'])#para remover a coluna constante e devolver ao datafrae sem a coluna 

nomedodataframe.info()#para ver os dados nulos 

nomedodataframe['coluna'].median()# para achar a mediana da coluna 

nomedodataframe = nomedodataframe['coluna'].fillna(nomedodataframe['coluna'].median())# substtiu os valores nulos pela mediana encontrada na coluna 

nomedodataframe.loc[nomedodataframe['coluna'] == '-', 'coluna'] = '0'#para substituir os dados erroneios


