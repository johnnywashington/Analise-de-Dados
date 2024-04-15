import numpy as np
import pandas as pd

df = pd.read_csv('houses.csv')#imprtar o dataset

df.head(20)#mostra as primeiras 20 linhas 

df.describe()#analise as estastiticas descritivas bases 

df['coluna'].value_counts()#para ver a distribuição da coluna PARA ANLISAR O POSSIVEL OUTLIERS

#OUTLIERS SAO PONTOS FORA DA CURVA NOS DADOS QUE PODEM DISTORCER AS ESTATISTICAS
#PARA IDENTIFICAR USACMOS O CRITERIO IQR Distancia inter quartil (Inter quantile range)
#outliers (valores discrepantes)
#inliers (internos)

q1 = df['coluna'].quantile(0.25) # Primeiro quartil para usar como referencia e eliminar o outlier abaixo dele
q3 = df['coluna'].quantile(0.75) # Primeiro quartil para usar como referencia e eliminar o outlier abaixo dele

IQR  = q3 - q1 # formula para achar o IQR

df_outliers = df[(df['coluna'] < q1 - (IQR * 1.5)) | (df['coluna'] > q3 + (IQR * 1.5))]
#essa é a estrutura para filtrar os outliers

df_inliers = df[(df['coluna'] >= q1 - (IQR * 1.5)) & (df['coluna'] <= q3 + (IQR * 1.5))]
# para remover o outliers