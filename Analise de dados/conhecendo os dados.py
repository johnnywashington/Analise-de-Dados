import numpy as np #como importar o numpy

import pandas as pd #como importar o pandas 

nomedodataframe = pd.read_csv('nome_da_pasta')# importar os arquivos datadseat(kaggle)

nomedodataframe.head()#Parar analisar as 5 primeiras linhas do dataframe

nomedodataframe.info()#Para ver as informaçoes dos dados por exemplo identficar dados nulls

nomedodataframe["nomedacoluna"].value_counts()#Para ler os dados de uma coluna e ver a frequencia dos dados

nomedodataframe[nomedodataframe['nomedacoluna'] == 'nomedosdados']#Para ver os dados de uma coluna e linha especifica 

nomedodataframe[nomedodataframe['nomedacoluna'] == 'nomedosdados']['nomedeoutracoluna'].mean()#para ver a media entre os dados desejados 


