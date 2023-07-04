import metodos.optimal_solution as optimal_solution

def findDiff(custos):
    linhaDiff = []
    colunaDiff = []
    for i in range(len(custos)):
        arr = custos[i][:]
        arr.sort()
        linhaDiff.append(arr[1]-arr[0])
    coluna = 0
    while coluna < len(custos[0]):
        arr = []
        for i in range(len(custos)):
            arr.append(custos[i][coluna])
        arr.sort()
        coluna += 1
        colunaDiff.append(arr[1]-arr[0])
    return linhaDiff, colunaDiff

# Complexidade O(2^n) 
def vogel(custos, oferta, demanda):
    INF = 10**3
    n = len(custos)
    m = len(custos[0])
    ans = 0
    bfs = []
    while max(oferta) != 0 or max(demanda) != 0:
        linha, coluna = findDiff(custos)
        maxi1 = max(linha)
        maxi2 = max(coluna)
    
        if(maxi1 >= maxi2):
            for ind, val in enumerate(linha):
                if(val == maxi1):
                    mini1 = min(custos[ind])
                    for ind2, val2 in enumerate(custos[ind]):
                        if(val2 == mini1):
                            mini2 = min(oferta[ind], demanda[ind2])
                            bfs.append(((ind, ind2), mini2))
                            ans += mini2 * mini1
                            oferta[ind] -= mini2
                            demanda[ind2] -= mini2
                            if(demanda[ind2] == 0):
                                for r in range(n):
                                    custos[r][ind2] = INF
                            else:
                                custos[ind] = [INF for i in range(m)]
                            break
                    break
            
        else:
            for ind, val in enumerate(coluna):
                if(val == maxi2):
                    mini1 = INF
                    for j in range(n):
                        mini1 = min(mini1, custos[j][ind])
    
                    for ind2 in range(n):
                        val2 = custos[ind2][ind]
                        if val2 == mini1:
                            mini2 = min(oferta[ind2], demanda[ind])
                            bfs.append(((ind2, ind), mini2))
                            ans += mini2 * mini1
                            oferta[ind2] -= mini2
                            demanda[ind] -= mini2
                            if(demanda[ind] == 0):
                                for r in range(n):
                                    custos[r][ind] = INF
                            else:
                                custos[ind2] = [INF for i in range(m)]
                            break
                    break
    return ans, bfs
 
# custos = [[1, 2, 3, 4], [4, 3, 2, 4], [0,2,2,1]] # table
# custos_temp = [[1, 2, 3, 4], [4, 3, 2, 4], [0,2,2,1]]
# oferta = [6,8,10]  # supply
# demanda = [4,7,6,7]  # demand
# ans, bfs = vogel(custos_temp,oferta,demanda)
# print(f'Custo usando o método de vogel: {ans}')
# print(f'Variáveis básicas:\n{bfs}')


# tabela_final = stepstone.transportation_simplex_method(custos, bfs)
# print(f'Tabela final:\n{tabela_final}')
# print(f'Custo mínimo: {stepstone.get_custo_total(custos, tabela_final)}')
