import numpy as np
import pandas as pd

def criaMatriz(nome_arquivo):

    arq = pd.read_excel(nome_arquivo)

    # Retira elementos da origem
    origem = arq['Unnamed: 0']
    arq.drop('Unnamed: 0', inplace=True, axis=1)
    arq = verificaSomatorio(arq)
    n = len(arq.index)

    # Salva em uma lista os valores de oferta
    oferta = arq.iloc[:n-1, -1].values.tolist()
    arq.drop('Oferta', inplace=True, axis=1)

    # Salva em uma lista os valores de demanda
    demanda = arq.iloc[-1].values.tolist()
    arq = arq.drop(arq.index[-1])
    custos = arq.values.tolist()
    return arq, origem, oferta, demanda, custos

def verificaSomatorio(arq):

    ultimo_elemento = arq.iloc[-1, -1]

    if(arq.iloc[-1, -1] < 0):
        nova_coluna = pd.Series([0] * (arq.shape[0] - 1) + [-ultimo_elemento], index=arq.index)
        arq.insert(arq.shape[1] - 1, "Artificial", nova_coluna)
        arq.iloc[-1,-1] = 0

    elif(arq.iloc[-1,-1] > 0):

        # Obter o índice da última linha
        indice_ultima_linha = len(arq) - 1

        # Criar a nova linha com todos os valores iguais a zero
        nova_linha = pd.Series(0, index=arq.columns)

        # Definir o último elemento da nova linha como 10
        nova_linha.iloc[-1] = abs(ultimo_elemento)

        # Inserir a nova linha antes da última
        arq = pd.concat([arq.loc[:indice_ultima_linha-1], pd.DataFrame([nova_linha]), arq.loc[indice_ultima_linha:]], ignore_index=True)

        # Inserir a nova linha na penúltima posição
        
        # # Criar uma nova linha com zeros na penúltima posição
        # nova_linha = pd.Series([0] * (arq.shape[1] - 1) + [ultimo_elemento], index=arq.columns)
        # arq = pd.concat([arq[:-1], nova_linha, arq.iloc[[-1]]], ignore_index=True)
        arq.iloc[-1,-1] = 0
    return arq

def geraArquivo(string,arq_t, origem, oferta, demanda_t, basicas):

    demanda = copiar_lista(demanda_t)
    arq = arq_t.copy()
    basicas = np.array(basicas)
    if basicas.shape == arq.shape:

        # Atualizar os valores do DataFrame com os valores da matriz
        for i in range(basicas.shape[0]):
            for j in range(basicas.shape[1]):
                arq.iloc[i, j] = basicas[i, j]

    arq.insert(0, '', origem)
    arq['Oferta'] = oferta

    if len(demanda) != len(arq.columns):

        # Adicionar valores padrão para colunas adicionais, se houver
        demanda.insert(0, 'Demanda') 
        num_colunas_faltantes = len(arq.columns) - len(demanda)
        demanda += [0] * num_colunas_faltantes   

    nova_serie = pd.Series(demanda, index=arq.columns)
    arq = pd.concat([arq, nova_serie.to_frame().T], ignore_index=True)

    # arq.iloc[-2, arq.columns.get_loc('')] = obter_proxima_letra(arq.iloc[-3, arq.columns.get_loc('')])
    arq.iloc[-2, arq.columns.get_loc('')] = 'Artificial'
    arq.to_excel(string, index=False)

def copiar_matriz(matriz):

    nova_matriz = []

    for linha in matriz:
        nova_linha = []
        for elemento in linha:
            nova_linha.append(elemento)
        nova_matriz.append(nova_linha)

    return nova_matriz

def copiar_lista(lista):

    nova_lista = []

    for elemento in lista:
        nova_lista.append(elemento)

    return nova_lista

def convert_to_matrix(data):

    max_x = max(data, key=lambda d: d[0][0])[0][0]
    max_y = max(data, key=lambda d: d[0][1])[0][1]
    matrix = np.zeros((max_x + 1, max_y + 1))

    for (x, y), value in data:
        matrix[x, y] = value

    return matrix

def obter_proxima_letra(letra):

    codigo_ascii = ord(letra.upper())
    codigo_ascii += 1

    if codigo_ascii > ord('Z'):
        codigo_ascii = ord('A')
        
    return chr(codigo_ascii)

