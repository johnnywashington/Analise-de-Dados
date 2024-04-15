import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns

df = pd.read_csv('node no dataseat')

df.info()#ao analisar que a data esta sendo interpretada como objeto, voce precisa coverter ela 

df['nomedacoluna'] = pd.to_datetime(df['nomedacoluna'])# isso ira converter de objeto para datetime

#ao identificar que tem muitos dados e no grafico nao fica bom crie um filtro para poder analisar 
df_filtered = df['coluna'] >= '2010-01-01'
ax = df_filtered.plot(x='coluna', y='linha', figsize=(12, 6))#para criar o grafico de acordo com o filtro

ax = df_filtered.plot(x='coluna', y='linha', figsize=(12, 6))
xcoords = ['2010-01-01', '2011-01-01', '2012-01-01', '2013-01-01', '2014-01-01', '2015-01-01']
#para gerar outro grafico tracando uma linha nos pontos onde acho importante 

for xc in xcoords:
    plt.axvline(x=xc, color='black', linestyle='--')

#para se aprofundar em uma modelagem estatisticas, decomposição de sacionalidade
from statsmodels.tsa.seasonal import seasonal_decompose #importando a biblioteca

df_filtered.set_index('coluna', inplace=True)#precisa converter o datetime para indice pois a funcao ira exigir isso 

analysis = df_filtered[['coluna']].copy()
decompose_result = seasonal_decompose(analysis, model='coluna')
trend = decompose_result.trend
seasonal = decompose_result.seasonal
residual = decompose_result.resid
#