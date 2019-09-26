frase = 'Curso em vídeo Python'
print(frase[3])
print(frase[:5])
print(frase[9:14])
print(frase[9:21])
print(frase[9:20:2])
print(frase[15:])
print(frase[9::3])
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())# tira espaços
print(frase.rstrip())# tira espaços da direita
print(frase.lstrip())# tira espaços da esquerda
print(frase.split())
print('-'.join(frase))