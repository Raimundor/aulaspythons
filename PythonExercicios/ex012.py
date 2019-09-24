n = float(input('Qual o preço do produto? R$ '))
d = n - (n * 5 / 100)# ou (n * 0.05)
print(f'O produto custava R${n:.2f}, na promoção com desconto de 5% vai custar R${d:.2f}')