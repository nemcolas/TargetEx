def inverter_string(s):

    # String começa vazia
    invertida = ""

    #Loop para inverter a string
    for i in range(len(s) - 1, -1, -1): # Logica que inverte a string, basicamente pega o tamanho da string e vai decrementando até chegar no primeiro caractere
        invertida += s[i]
    return invertida

# Entrada: String a ser invertida
string = input("Informe a string: ")

# Resultado
print(f"String invertida: {inverter_string(string)}")
