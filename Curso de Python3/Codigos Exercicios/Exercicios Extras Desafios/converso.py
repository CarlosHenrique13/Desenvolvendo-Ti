real = float(input("QUANTO DINHEIRO VOCE TEM NA CARTEIRA? R$ "))
#Valor do Dolar do Dia 
dolar_hoje = 5.07
dolar = real / dolar_hoje
print("COM R${} VOCE PODE COM USS{:.2}".format(real,dolar))
