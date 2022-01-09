# String
nome = str(input("Nome: "))
# Inteiros
idade = int(input("Idade: "))
# Flutuantes
peso = float(input("Peso: : "))
# booleanos
sexo = input("Sexo True para Masculino False para Feminino: ")
print("Nome: ",nome)
print("Idade",idade)
print("Peso",peso)

if sexo == True:
    print(f"Masculino")
else:
    print(f"Feminino")
