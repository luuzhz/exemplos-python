def calculo(total_conta,pessoas):
    resultado = total_conta / pessoas
    return resultado

print("Seja Bem vindo ao Restaurante Caio Burguer")
total_conta = float(input("Digite o Valor da Conta: "))
pessoas = int(input("Digite a quantidade de Pessoas que a conta, será dividido: "))
print(f"O valor a ser pago por cada um é :{calculo(total_conta,pessoas)}")
