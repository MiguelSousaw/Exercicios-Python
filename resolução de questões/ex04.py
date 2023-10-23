nome = input('Escreva seu nome')
n1 = float (input ('Escreva sua primeira nota'))
n2 = float (input ('Escreva sua segunda nota'))
n3 = float (input ('Escreva sua terceira nota'))
media=int ((n1+n2+n3)/3)
if media >=6:
   print (media,"aprovado")
else: 
    print(media,'reprovado')