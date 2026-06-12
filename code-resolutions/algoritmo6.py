# Problema 6 - Verificando Palíndromos
# Descrição: Testar se uma palavra é um palíndromo?! Dica: Utilizar conceitos de manipulação de strings para inverter a palavra e comparar com a original.

palavra = input("Digite uma palavra: ").lower()

palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print(f"'{palavra}' é um PALÍNDROMO!")
else:
    print(f"'{palavra}' NÃO é um palíndromo.")
    print(f"Palavra Invertida: '{palavra_invertida}'")

