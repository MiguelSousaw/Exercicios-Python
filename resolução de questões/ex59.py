par = 0
impar = 0
for c in range (1,11):
   num = int (input('Digite um número inteiro: '))
   if num % 2== 0:
      par += 1
   if num % 2 == 1:
      impar += 1
print (f'Dos números digitados {par} são par e {impar} são impar')
