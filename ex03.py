import json

# Carregar arquivo JSON com faturamento
with open('faturamento.json') as file:
    faturamento = json.load(file)

# Filtrar apenas os dias com faturamento
valores = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

# Cálculos de faturamento
menor_faturamento = min(valores)
maior_faturamento = max(valores)
media_faturamento = sum(valores) / len(valores)
dias_acima_media = len([valor for valor in valores if valor > media_faturamento])

# Resultados dos cálculos
print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
