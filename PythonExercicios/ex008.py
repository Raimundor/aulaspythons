n = float(input('Um distância em metros: '))
print(f'A medida de {n:.1f}m corresponde a '
      f'\n{n/1000}km '
      f'\n{n/100}hm'
      f'\n{n/10}dam'
      f'\n{n*10:.0f}dm'
      f'\n{n*100:.0f}cm'
      f'\n{n*1000:.0f}mm')