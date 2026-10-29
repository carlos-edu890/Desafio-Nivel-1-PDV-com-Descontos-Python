lista = []
comprasRealizadas = 0

while True:
  idade = int(input("Sua idade: "))

  valorCompra = float(input("Valor da compra: "))

  valorFinal = valorCompra
  valorDesconto = 0

  if valorCompra > 0 and idade >= 0:
    if idade >= 65:
      valorFinal = valorFinal - (valorFinal * 0.2)
      valorDesconto = valorDesconto + 20

    if valorFinal > 100:
      valorFinal = valorFinal - (valorFinal * 0.1)
      valorDesconto = valorDesconto + 10

    print(f"O valor final foi R$ {valorFinal:.2f}")
  elif valorCompra < 0 or idade < 0:
    print("O valor de compra e a idade devem ser maiores ou iguais a zero.")
  else:
    break

  comprasRealizadas += 1
  lista.append([valorCompra, valorDesconto, valorFinal])


totalValorCompras = 0
totalValorFinal = 0
totalDesconto = 0
for compra in lista:
  totalValorCompras += compra[0]
  totalDesconto += compra[1]
  totalValorFinal += compra[2]

print(f"Total de compras feitas: {comprasRealizadas}\nTotal bruto: R$ {totalValorCompras:.2f}\nTotal de descontos concedidos: {totalDesconto}%\nTotal final: R$ {totalValorFinal:.2f}")