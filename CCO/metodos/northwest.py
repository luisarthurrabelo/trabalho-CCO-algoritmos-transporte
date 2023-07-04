import metodos.optimal_solution as optimal_solution

# Complexidade(2^n)
def noroeste(custos, oferta, demanda):
    ans = 0
    linha = 0 
    coluna = 0
    bfs = []
    while(linha != len(custos) and coluna != len(custos[0])):

        if(oferta[linha] <= demanda[coluna]):
            ans += oferta[linha] * custos[linha][coluna]
            demanda[coluna] -= oferta[linha]
            bfs.append(((linha, coluna), oferta[linha]))
            linha += 1
        else:
            ans += demanda[coluna] * custos[linha][coluna]
            oferta[linha] -= demanda[coluna]
            bfs.append(((linha, coluna), demanda[coluna]))
            coluna += 1 
    return ans, bfs
    
# custos = [[1, 2, 3, 4], [4, 3, 2, 4], [0,2,2,1]] # table
# custos_temp = [[1, 2, 3, 4], [4, 3, 2, 4], [0,2,2,1]]
# oferta = [6,8,10]  # supply
# demanda = [4,7,6,7] # demand
