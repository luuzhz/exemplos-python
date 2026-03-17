# desconto_produto.py

# Recebendo os dados
descricao = input("Digite a descrição do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: "))

# Calculando o total sem desconto
total = quantidade * preco_unitario

# Verificando o desconto
if quantidade <= 5:
    desconto = total * 0.02
elif quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05

# Calculando total a pagar
total_pagar = total - desconto

# Exibindo resultados
print("\nProduto:", descricao)
print("Total sem desconto: R$", total)
print("Desconto: R$", desconto)
print("Total a pagar: R$", total_pagar)