vogal = ['a', 'e', 'i', 'o', 'u']
consoante = 0
for i in range (10):
    caracter = str(input('Escreva um caracter: ')).lower().strip()[0]
    if caracter not in vogal:
        consoante += 1
print (f'Existem {consoante} consoantes na cadeia de caracter!')