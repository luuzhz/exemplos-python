import os
os.system ("cls")

#Criando as Funçõesdef exibir_menu ():
def exibir_menu():
    print("=== Conversor de Moedas ===")
    print("[1] - Converter Dolar -> Real")
    print("[2] - Converter Real -> Dolar")
    print ("[3] - Sair")
def converter_dolar_para_real (quantia_dolar, cotacao):
    total_real = quantia_dolar * cotacao
    return total_real
def converter_real_para_dolar (quantia_reais, cotacao):
    total_dolares = quantia_reais / cotacao
    return total_dolares
def sair():
    exit()

def limpar_tela():
    os.system("cls")
def main():
    exibir_menu()
    opcao = int(input("Escolha um opção: "))
    if opcao == 1:
        quantia_dolar = float(input("Digite a Quantidade de Dolares: "))
        cotacao = float(input("Digite a Cotação: "))
        resultado = converter_dolar_para_real(quantia_dolar,cotacao)
        print(f"O Total da Conversão é: R${resultado}")
    if opcao == 2:
        quantia_reais = float(input("Digite a Quantia De Reais: "))
        cotacao = float(input("Digite a Cotação: "))
        converter_real_para_dolar()
    if opcao == 3:
        exit
    
    
main()