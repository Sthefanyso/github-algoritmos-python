# Problema 3 - Operações Matemáticas Simples
# Descrição: Solicitar como entrada dois números e depois realizar uma operação simples entre eles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha uma operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 == 0:
        print("Erro: divisão por zero não é permitida.")
        resultado = None
    else:
        resultado = num1 / num2
else:
    print("Operação inválida. Use +, -, * ou /.")
    resultado = None

if resultado is not None:
    print(f"Resultado de {num1} {operacao} {num2} = {resultado}")

