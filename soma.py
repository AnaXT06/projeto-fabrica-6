imposto = float(input("Digite o imposto"))
valor = float(input("Digite o valor"))

preco_final = valor + (valor*(imposto/100))
print(preco_final)