dias = int(input("Qauntos dias alugados? "))
km = float(input("Quantos Km rodados? "))
pago = (dias*60) + (km * 0.15)
print('O total a pagar éde R${:.2f}'.format(pago))