import pandas as pd
import numpy as np

def criar_tabela(nome1, nome2):

    # Carregar a planilha do Excel em um DataFrame
    df = pd.read_excel(nome1)
    temp = pd.DataFrame()
    temp[''] = ''
    i = 1

    # Iterar sobre as linhas do DataFrame
    for index, row in df.iterrows():

        if not(pd.isnull(row['Demanda']) or pd.isnull(row['Oferta'])):
            temp.at[i, ''] = row['Unnamed: 0']
            i+=1
            temp[row['Unnamed: 0']] = np.nan
        elif pd.isnull(row['Demanda']):
            temp.at[i, ''] = row['Unnamed: 0']
            i+=1
        else:
            temp[row['Unnamed: 0']] = np.nan

    temp.at[i, ''] = "Demanda"
    temp['Oferta'] = np.nan
    soma = max(df['Oferta'].sum(), df['Demanda'].sum())

    i = 1

    # Iterar sobre as linhas do DataFrame
    for index, row in df.iterrows():
        if not(pd.isnull(row['Demanda']) or pd.isnull(row['Oferta'])):
            temp.at[i, 'Oferta'] = soma
            i+=1
            temp.loc[temp.index[-1], row['Unnamed: 0']] = soma
        elif pd.isnull(row['Demanda']):
            temp.at[i, 'Oferta'] = row['Oferta']
            i+=1
        else:
            temp.loc[temp.index[-1], row['Unnamed: 0']] = row['Demanda']

    temp.iloc[-1, -1] = temp.iloc[-1, 1:].sum() - temp['Oferta'].sum()

    custos = pd.read_excel(nome2)
    bigM = int(max(custos['Custo'].dropna())) * 50
    bigM = 500
    temp = temp.fillna(bigM)
    for index, row in custos.iterrows():
        for index2, row2 in temp.iterrows():
            if(row['Envio'] == row2['']):
                temp.loc[index2, row['Chegada']] = row['Custo']
                
    for index, row in temp.iterrows():
        if (row[''] in temp.columns):
            temp.loc[index, row[''] ]= 0

    temp.to_excel("tabelas/dados.xlsx", index=False)