import os
import time
os.system ("cls")
banco_ligado = True
saldo = 0
while banco_ligado :
    print("Olá, Qual sua proxima ação no caixa Brasil.")
    print("1-Ver saldo")
    print("2-Depositar")
    print("3-Sacar")
    print("4-Sair")
    escolha = int(input("Escolha Por Favor: "))
    if escolha == 1:
        time.sleep (2)
        print(f"{saldo} esse é o saldo da sua conta")
        print("Você gostaria de Finalizar agora ou não?")
        print("1-Voltar para o inicio")
        print("2-Acabar")
        seg_escolha = int(input("Digite sua escolha: "))
        if seg_escolha == 2:
            banco_ligado = False
  
    elif escolha == 2:
        deposito = float(input("Quanto você gostaria de Depositar: "))
        saldo += deposito
        time.sleep (2)
        print(f"Você depositou com sucesso {deposito}")
        print("Você gostaria de Finalizar agora ou não?")
        print("1-Voltar para o inicio")
        print("2-Acabar")
        seg_escolha = int(input("Digite sua escolha: "))
        if seg_escolha == 2:
            banco_ligado = False
    elif escolha == 3:
        print ("Quanto você gostaria de Retirar da sua conta?")
        retirar = float(input("Digite: "))
        saldo = saldo - retirar
        time.sleep (2)
        print(f"Você retirou {retirar} da sua conta.")
        print("1-Voltar para o inicio")
        print("2-Acabar")
        seg_escolha = int(input("Digite sua escolha: "))
        if seg_escolha == 2:
            banco_ligado = False
    elif escolha == 4:
        print ("Sistema desligando")
        time.sleep (3)
        print("Até a proxima")
        banco_ligado = False


