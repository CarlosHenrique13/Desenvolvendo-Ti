# Tinta 1L = 3M, 1 Lata de Tinta 18L = 54 Metros
metros_q = float(input("Metros quadrados a pintar: "))

# Valores de Calculo da Tinta
valor_lata = 80
metros_por_litro = 3
lata_litros = 18
lata_pinta = metros_por_litro * lata_litros
quantidade_lata =  round(metros_q / lata_pinta)

# Saida para o usuario
if 0 == quantidade_lata:
    print(f"Quantidade de Latas: 1 e vai custar R$ {valor_lata}")
else:
    print(f"Quantidade de Latas: {quantidade_lata} e vai custar R$ {quantidade_lata*valor_lata}")


