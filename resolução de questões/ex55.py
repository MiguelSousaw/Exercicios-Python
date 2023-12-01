from time import sleep
print ('-='*30)
print ('O program a seguir irá imprimir o intervalo entre o número incial e o númeor final')
print ('-='*30)
n1 = int (input('Digite o número inicial: '))
n2 = int (input('Digite o númeor final:'))
print (f'O intervalo dos números {n1} e {n2} é...')
sleep (2)
for inter in range (n1+1, n2):
    print (inter, end = ' ')
