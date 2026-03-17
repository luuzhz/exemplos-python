import os

os.system("cls")
print("Ola Seja Bem vindo ao site Boletim Virtual")
 
nome = input("Coloque o seu Nome: ")
valor01 = int(input("Coloque a Primeira Nota do Bimestre: "))
valor02 = int(input("Coloque a Segunda Nota do Bimestre: "))
valor03 = int(input("Coloque a Terceira Nota do Bimestre: "))
 
Nota_final = (valor01 + valor02 + valor03) / 3
 
print("Sua nota Final foi :", Nota_final)
 
if Nota_final >= 7:
    print("Parabens",nome) 
    print(" Você Passou de Ano")
elif Nota_final >= 5:
        print("Sinto informar "),nome
        print("Você está de Recuperação")
else:
        print("Você está Reprovado")