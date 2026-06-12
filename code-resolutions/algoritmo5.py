# Problema 5 - Calculando Média de Notas
# Descrição: Calcular a média de três notas fornecidas na entrada do usuário. Dica: Utilize operadores aritméticos para realizar o cálculo da média.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média: {media:.2f}")
