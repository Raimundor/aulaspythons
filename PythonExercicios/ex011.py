lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lar * alt
tinta = area/2
print(f'Sua parede tem a dimensão de {lar}x{alt} e sua área é de {area}m².'
      f'\nPara pintar sua parede, você precisará de {tinta}l de tinta.')
