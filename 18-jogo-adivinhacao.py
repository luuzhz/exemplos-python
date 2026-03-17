import random

numero = random.randint(1, 10)
palpite = int(input("Digite seu palpite (1 a 10): "))

if palpite == numero:
    print("Acertou!")
else:
    print(f"Errou! Número era: {numero}")