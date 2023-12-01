num = int (input('Digite um número: '))
tot = 0
for c in range (1, num+1):
    if num % c == 0:
      print ('\033[033m', end = ' ')
      tot += 1
    else:
      print ('\033[031m', end = ' ')
    print (f'{c}', end = ' ')
print (f'\n\033[mO número {num} foi divisivel {tot} vezes')
if tot == 2:
    print (f'O número {num} é um número primo')
else:
    print (f'O número {num} nâo é um número primo')
    
