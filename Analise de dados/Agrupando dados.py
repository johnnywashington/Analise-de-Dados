import numpy as np #como importar o numpy

import pandas as pd #como importar o pandas 

nomedodataframe = pd.read_csv('nome_da_pasta')#importar o dataseat

nomedodataframe.head()#5 primeiras linhas do dataframe

nomedodataframe.describe()#Calcula a media de algumas decrições entre as colunas 

nomedodataframe['nomedacoluna'].value_counts()#Para medir a frequencia de quantas vezes aparece 

numeric_cols = nomedodataframe.select_dtypes(include=np.number)# para pedir apenas as colunas que o numpy considera numerica

numeric_cols = nomedodataframe.select_dtypes(include=np.number).columns.to_list()# para pedir as colista e trasnformar em lista

#apos isso podemos usar a função groupyby ...listadecolunascalculo
nomedodataframe.groupby(['listadecolunas'])[numeric_cols].mean()#para fazer a media para cada coluna usando a funcao agregada

nomedodataframe.groupby(['listadecolunas', 'outracoluna'])[numeric_cols].mean()#aqui ele vai agrupar mais de uma coluna e fazer a media 