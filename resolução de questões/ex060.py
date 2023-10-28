termos = int(input('Digite até que termo da serié de fibonacci se repita a sequência: '))
número = 1
número_ant=0
print(f'A sequência de fibonacci com {termos} termos é a seguinte: ' )
for _ in range(termos):
    print (número)
    ax = número
    número += número_ant
    número_ant = ax