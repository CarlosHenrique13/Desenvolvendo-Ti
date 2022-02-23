nome = str(input("DIGITE SEU NOME COMPLETO???  ")).strip()
print("Analisando seu nome...")
print("Seu nome mausculo  {} ".format(nome.upper()))
print("Seu nome em minusculo {}".format(nome.lower()))
print("Seu nome ao todo {} letras".format(len(nome)-nome.count(" ")))
print("Seu primeiro nome {} letras".format(nome.find(' ')))

