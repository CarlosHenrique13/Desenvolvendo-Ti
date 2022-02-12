nota_1 = float(input("Digite a 1° Nota: "))
nota_2 = float(input("Digite a 2° Nota: "))

nota_final = (nota_1+nota_2)/2

if nota_final == 7:
    print(f"O Aluno foi Aprovado com Nota: {nota_final}")
elif nota_final < 7:
    print(f"O Aluno foi Reprovado com Nota: {nota_final}")
elif nota_final == 10:
    print(f"O Aluno foi Aprovado com Distinção com Nota: {nota_final}")
    

