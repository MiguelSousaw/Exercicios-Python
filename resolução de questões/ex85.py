from time import sleep
print ('-='*20)
print ('ELEIÇÃO')
print ('''CANDIDATOS:
[1] JOSÉ
[2] JOÃO
[3] SARTO
[4] ELMANO
[5] NULO
[6] BRANCO''')
print ('-='*20)
jose = elmano = sarto = joao = nulo = branco = voto = tot = 0
while True:
    voto = int (input('INSIRA O NÚMERO DO RESPECTIVO CANDIDATO A SER VOTADO: '))
    if voto == 0:
        break
    if voto == 1:
       jose += 1
    if voto == 2:
        joao += 1
    if voto == 3:
        sarto += 1
    if voto == 4:
        elmano += 1
    if voto == 5:
        nulo += 1
    if voto == 6:
        branco += 1
print(f'VOTAÇÃO FINALIZADA...')
print (f'-='*20)
print ('PROCESSANDO RESULTADO')
sleep (3)
print (f'''Candidato Jose: [{jose}]Votos
Candidato João [{joao}]Votos
Candidato Elmano [{elmano}]Votos
Candidato Sarto [{sarto}]Votos
Votos em nulo: [{nulo}]
Votos em branco [{branco}]''')
print ('-='*20)
if jose > joao and jose > elmano and jose > sarto:
   
   print (f'O vencedor foi José com {jose} votos')
elif joao > jose and joao > sarto and joao > elmano:
    print (f'O vencedor foi João com {joao} votos')
elif sarto > jose and sarto > joao and sarto > elmano:
    print (f'O vencedor foi Sarto com {sarto} votos')
elif elmano > sarto and elmano > joao and elmano > jose:
    print (f'O vencedor foi Elmano com {elmano} votos')
else:
    print ('O RESULTADO DESSA ELEIÇÃO FOI EMPATADO')
print ('-='*20)
tot = elmano + jose + sarto + joao
porcento_nulo = (nulo*100)/tot
porcento_branco = (branco*100)/tot
print (f'A porcentagem de votos brancos com relação ao total de votos é {porcento_branco:.2}%')
print (f'A porcentagem de votos nulos com relação ao total de votos é {porcento_nulo:.2}%')
    

