larg = float(input("LARGURA DA PAREDE :"))
alt = float(input("ALUTURA DA PAREDE :"))
area = larg * alt 
print("SUA PAREDE TEM DIMENSAO DE {}X{}E SUA AREA E DE {:.2f}m".format(larg,alt,area))
tinta = area / 2
print("para pintar esa parede voce precisara de {:.2f}l de tinta ".format(tinta))
