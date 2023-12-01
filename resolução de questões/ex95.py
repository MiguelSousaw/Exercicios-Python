caracter = []
consoante = 0
for i in range (10):
    caracter.append(input('Digite uma letra: ')[0])
for c in caracter:
    c = c.upper()
    if c != 'A' and c != 'E' and c != 'I' and c != 'O' and c != 'U':
        consoante += 1
        print (c, end = ' ')
print (f'Foram lidas {consoante} consoantes.')
