# atribuindo os valores do faturamento junto com do estado em um dicionário
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calculo do percentual de faturamento por estado
total_faturamento = sum(faturamento_estados.values())

# Loop para calcular o percentual de faturamento por estado
for estado, valor in faturamento_estados.items():
    percentual = (valor / total_faturamento) * 100 #Logica para calcular o percentual
    print(f"{estado}: {percentual:.2f}%")
