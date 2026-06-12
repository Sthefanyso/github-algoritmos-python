# Problema 4 - Verificando Números Pares e Ímpares
# Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")

