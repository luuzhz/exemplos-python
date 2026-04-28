
import os
os.system("cls")
#Criando a Primeira função
def escreva():
    print("Ola Mundo!")
#chamando a função
escreva()

#criando função com parametro
def exibir_dados(nome,idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print ("=" * 200)
exibir_dados("Caio",45)
#Criando uma Função com retorno
def somar (n1,n2):
    resultado = n1 + n2
    return resultado
#Ela excecuta e guarda o valor
#chamando a função
total = somar(10,20)
print(f"O total será: {somar(10,20)}")