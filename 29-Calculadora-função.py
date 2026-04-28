import os
os.system ("cls")
def somar(numero1,numero2):
    resultado = numero1 + numero2
    return resultado
def Subtrair(numero1,numero2):
    resultado = numero1 - numero2
    return resultado

def Multiplicar(numero1,numero2):
    resultado = numero1 * numero2
    return resultado

def Dividir(numero1,numero2):
    resultado = numero1 / numero2
    return resultado

def encerrar():
    print("Operação invalida!")
    input("Pressione enter Para finalizar...")


print("Seja Bem Vindo a Super Calculador 2.0.67")

numero1 = int(input("Digite o primeiro Numero: "))
numero2 = int(input("Digite o Segundo Numero: "))
print("Escolha Uma Das Opções Abaixo")
print("[1] - Somar")
print("[2] - Subtrair")
print("[3] - Multiplicar")
print("[4] - Dividir")
opção = int(input("Escolha uma opção: "))

if (opção == 1):
    print(f"A Soma é: {somar(numero1,numero2)}")
if (opção == 2):
    print(f"A Subtração é: {Subtrair(numero1,numero2)}")
if (opção == 3):
    print(f"A Multiplicação é: {Multiplicar(numero1,numero2)}")
if (opção == 4):
    print(f"A Divisão é: {Dividir(numero1,numero2)}")
else :
    encerrar()