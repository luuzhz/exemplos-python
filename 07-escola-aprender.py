# Recebendo os dados
nivel = int(input("Digite o nível do professor (1, 2 ou 3): "))
aulas_semana = int(input("Digite a quantidade de aulas por semana: "))

# Definindo o valor da hora/aula
if nivel == 1:
    valor_hora = 12.00
elif nivel == 2:
    valor_hora = 17.00
elif nivel == 3:
    valor_hora = 25.00
else:
    print("Nível inválido!")
    exit()

# Considerando 4 semanas no mês
salario = valor_hora * aulas_semana * 4

# Exibindo o resultado
print(f"Salário mensal: R$ {salario:.2f}")