# Problema 8 - Somando Valores de uma Lista
# Descrição: Receber uma sequência de números inteiros separados por espaço e exibir a soma de todos eles.

numeros = list(map(int, input("Digite os números separados por espaço: ").split()))

soma = 0

for numero in numeros:
    soma += numero

print(f"A soma dos valores é: {soma}")