import os
os.system ("cls")

numero = int(input("Digite um Numero: "))
vezes = int(input("Até que numero você quer: "))
contador = 0
while(contador <= vezes):
    print(f"{numero} x {contador} = {numero * contador}")
    contador+=1
