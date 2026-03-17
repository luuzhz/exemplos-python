tipo = int(input("Tipo de veículo (1-Carro, 2-Moto, 3-Caminhão): "))

if tipo == 1:
    print("Pedágio: R$10")
elif tipo == 2:
    print("Pedágio: R$5")
elif tipo == 3:
    print("Pedágio: R$20")
else:
    print("Tipo inválido")
