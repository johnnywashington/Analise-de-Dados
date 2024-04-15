import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

df = sns.load_dataset('iris')#importar um dos datasets de flores, famosos para estudos

df.head()# para ver os primeiros dados 

col = 'coluna'
sns.histplot(data=df, x=df['coluna']).set_title(f'Distribuição da variavel {col}')#para cariar um grafico histograma (grafico de frequencia )
#set.title é para colocar titulo no gráfico 

for col in  df.drop(columns='coluna'):
    sns.histplot(data=df, x=df['col'], kds=True, hue=['coluna']).set_title(f'Distribuição da variavel {col}')
    plt.show()
    #para ver um grafico com a distribuição de cada linha em histograma

for col in  df.drop(columns='coluna'):
    sns.barplot(data=df, x=df['col'], hue=['coluna'], y= col, ci= 90)
    plt.show()
    #para ver um grafico que mostra a media e o ci (intervalo de confiança)

    # com esses exemplos podemos avaliar as variaveis categoricas 




