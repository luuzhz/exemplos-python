import os
os.system ("cls")
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
   
if(idade >=18):
        habilitacao = int(input("Possui Habilitação? (1- Sim ou 2-Não):"))
   
        if(habilitacao == 1):
            print("Você pode dirgir!")
        else:
            print("Você não possui Habilitação")
else:
        print("Você é menor de idade")  
 
resposta = input("Você gostaria de executar o programa novamente? (S/N): ")

resposta = "S"
 
while resposta == "S":
    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade:"))
   
    if(idade >=18):
        habilitacao = int(input("Possui Habilitação? (1- Sim ou 2-Não):"))
   
        if(habilitacao == 1):
            print("Você pode dirgir!")
        else:
            print("Você não possui Habilitação")
    else:
        print("Você é menor de idade")  
 
    resposta = input("Você gostaria de executar o programa novamente? (S/N): ")
 
print("Espero ter ajudado!")