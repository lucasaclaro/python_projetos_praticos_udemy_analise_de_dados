import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_base = pd.read_csv('data/Startups+in+2021+end.csv')
#print(data_base.shape) #verificar a qtd de linhas e colunas

#print(data_base.head()) #vefificar os primeiros 5 registros

#print(data_base.columns) #verificar as colunas

data_base.rename(columns={'Unnamed: 0': 'Id'}, inplace=True) #renomear a coluna

#print(data_base.info()) #verificar os tipos de dados.

#Nessa base de dados existem tipos de dados que precisam ser alterados para números inteiros e existem também valores nulos em algumas linhas

#print(data_base.isnull().sum()) #verificar onde estão os valores nulos. Existem 15 no campo City e 1 no campo Select Investors

#print(data_base.nunique()) #verificar quantos campos únicos

#print(data_base['Industry'].unique()) #exibir os campos únicos

#print(data_base['Industry'].value_counts()) #rankear as empresas que mais aparecem

#print(data_base['Industry'].value_counts(normalize=True)) #exibe os valores acima em porcentagem


#Criar gráfico do ranking dos setores das empresas Unicórnio
#plt.figure(figsize=(15, 6))
#plt.title('Sector Ranking of Unicorn company')
#plt.bar(data_base['Industry'].value_counts().index, data_base['Industry'].value_counts())
#plt.xticks(rotation=45, ha='right') #como as informações da base do gráfico ficaram muito agrupadas, é possível rotacionar a exibição dos valores para melhorar a visualização
#plt.show()

#print(data_base['Country'].unique()) #exibe os campos únicos de países

#print(data_base['Country'].value_counts()) #rankear os países que mais aparecem

analysis_city = round(data_base['Country'].value_counts(normalize=True) * 100, 1)
#print(analysis_city) #exibe os valores em porcentagem


#Criar gráfico de pizza do ranking de países
#plt.figure(figsize=(15, 6))
#plt.title('Countries of Unicorn company')
#plt.pie(
#    analysis_city,
#    labels=analysis_city.index,
#    shadow=True,
#    startangle=90,
#    autopct='%1.1f%%' #colocar o valro dentro do gráfico de pizza
#)
#plt.show()

#Criar gráfico de pizza do ranking dos 10 primeiros países
#plt.figure(figsize=(15, 6))
#plt.title('Countries of Unicorn company')
#plt.pie(
#    analysis_city.head(10),
#    labels=analysis_city.index[0:10],
#    shadow=True,
#    startangle=90,
#    autopct='%1.1f%%' #colocar o valro dentro do gráfico de pizza
#)
#plt.show()

#Conversor de valores para data
data_base['Date Joined'] = pd.to_datetime(data_base['Date Joined'])
#print(data_base['Date Joined'].head())

#Criar as colunas mês e ano, extraindo o mês e ano da coluna Date Joined
data_base['Month'] = pd.DatetimeIndex(data_base['Date Joined']).month
data_base['Year'] = pd.DatetimeIndex(data_base['Date Joined']).year
#print(data_base.columns) #verificar as colunas

analysis_date = data_base.groupby(by=['Country', 'Year', 'Month', 'Company']).count()['Id'].reset_index() #agrupamento de algumas colunas, contando elas, exibindo o Id e resetando o index
#print(analysis_date.loc[analysis_date['Country'] == 'Brazil']) #exibe os dados apenas das linhas em que a coluna é Brazil

data_base['Valuation ($B)'] = pd.to_numeric(data_base['Valuation ($B)'].apply(lambda linha: linha.replace('$', '')))#retirar o $ da coluna Valuation
#A função apply no Pandas permite percorrer linha por linha e efetuar alguma ação e a função to_numeric transforma o valor em número
print(data_base['Valuation ($B)'])


#https://www.udemy.com/course/python-para-analise-de-dados/learn/lecture/31425290#overview