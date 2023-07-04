import controlededados.coletadados as coletadados
import metodos.vogel as vogel
import metodos.minimum_cost as minimum_cost
import metodos.northwest as northwest
import metodos.optimal_solution as optimal_solution
import transposto

#transposto.criar_tabela('tabela.xlsx', 'tabela_custos.xlsx')
#transposto.criar_tabela('tabela_artificial.xlsx', 'tabela_artificial_custos.xlsx')
transposto.criar_tabela('exemplo_distribuidoradejogos.xlsx', 'exemplo_distribuidoradejogos_custos.xlsx')
arq, origem, oferta, demanda, custos = coletadados.criaMatriz("tabelas/dados.xlsx")

print("#############################################################")
print("                          VOGEL")
custos_temp = coletadados.copiar_matriz(custos)
oferta_temp = coletadados.copiar_lista(oferta)
demanda_temp = coletadados.copiar_lista(demanda)
ans, bfs = vogel.vogel(custos_temp,oferta_temp,demanda_temp)
bfs_temp = coletadados.copiar_matriz(bfs)
print(f'Custo usando o método de vogel: {ans}')
print(f'Variáveis básicas:\n{bfs}')
tabela_final = optimal_solution.transportation_simplex_method(custos, bfs_temp)
print(f'Tabela final:\n{tabela_final}')
print(f'Custo mínimo: {optimal_solution.get_custo_total(custos, tabela_final)}')
coletadados.geraArquivo("tabelas/resultado_vogel.xlsx",arq,origem,oferta,demanda, coletadados.convert_to_matrix(bfs))

print("#############################################################")
print("                      MINIMO DOS CUSTOS")
custos_temp = coletadados.copiar_matriz(custos)
oferta_temp = coletadados.copiar_lista(oferta)
demanda_temp = coletadados.copiar_lista(demanda)
ans, bfs = minimum_cost.minimo_custo(custos_temp,oferta_temp,demanda_temp)
bfs_temp = coletadados.copiar_matriz(bfs)
print(f'Custo usando o método de minimo dos custos: {ans}')
print(f'Variáveis básicas:\n{bfs_temp}')
print(f'Tabela final:\n{tabela_final}')
print(f'Custo mínimo: {optimal_solution.get_custo_total(custos, tabela_final)}')
coletadados.geraArquivo("tabelas/resultado_minimo.xlsx",arq,origem,oferta,demanda, coletadados.convert_to_matrix(bfs))

print("#############################################################")
print("                      CANTO NOROESTE")
custos_temp = coletadados.copiar_matriz(custos)
oferta_temp = coletadados.copiar_lista(oferta)
demanda_temp = coletadados.copiar_lista(demanda)
ans, bfs = northwest.noroeste(custos_temp, oferta_temp, demanda_temp)
bfs_temp = coletadados.copiar_matriz(bfs)
print(f'Custo usando o método do canto noroeste: {ans}')
print(f'Variáveis básicas:\n{bfs_temp}')
tabela_final = optimal_solution.transportation_simplex_method(custos, bfs_temp)
print(f'Tabela final:\n{tabela_final}')
print(f'Custo mínimo: {optimal_solution.get_custo_total(custos, tabela_final)}')

coletadados.geraArquivo("tabelas/resultado_noroeste.xlsx",arq,origem,oferta,demanda, coletadados.convert_to_matrix(bfs))

coletadados.geraArquivo("tabelas/resultado_otimo.xlsx",arq,origem,oferta,demanda, tabela_final)