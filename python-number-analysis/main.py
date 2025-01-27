def calcular_estatisticas(numeros):
    pares = len([num for num in numeros if num % 2 == 0])
    impares = len([num for num in numeros if num % 2 != 0])
    media = sum(numeros) / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    return media, maximo, minimo, pares, impares

numeros = []
for _ in range(10):
    numero = int(input("Digite os numeros: "))
    numeros.append(numero)

estatisticas = calcular_estatisticas(numeros)

print("Média, número máximo, número mínimo, quantidade de pares e ímpares ", estatisticas)
