# Problema 2 - Repetindo textos
# Descrição: solicitar uma string e um número inteiro como entrada. Retornar como resultado a string repetida o número de vezes informado.

texto = input("Digite uma palavra: ")
vezes = int(input("Digite um número inteiro: "))

print("Resultado:")
for i in range(vezes):
    print(texto)

