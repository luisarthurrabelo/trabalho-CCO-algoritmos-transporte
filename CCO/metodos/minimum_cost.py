import metodos.optimal_solution as optimal_solution

# Completaxidade O(2^n)
def minimo_custo(custos, oferta, demanda):
    ans = 0
    bfs = []
    INF = 10**3
    n = len(custos)
    m = len(custos[0])
    while max(oferta) != 0 or max(demanda) != 0:
        mini1 = INF
        for i in range(n):
            for j in range(m):
                if (custos[i][j] < mini1 and oferta[i] > 0 and demanda[j] > 0):
                    mini1 = custos[i][j]
                    ind1, ind2 = i, j
        mini2 = min(oferta[ind1], demanda[ind2])  
        bfs.append(((ind1, ind2), mini2)) 
        ans += mini2 * mini1
        oferta[ind1] -= mini2
        demanda[ind2] -= mini2
        custos[ind1][ind2] = INF

    return ans, bfs

# custos = [[1, 2, 3, 4], [4, 3, 2, 4], [0,2,2,1]] # table
# custos_temp = [[1, 2, 3, 4], [4, 3, 2, 4], [0,2,2,1]]
# oferta = [6,8,10]  # supply
# demanda = [4,7,6,7]  # demand