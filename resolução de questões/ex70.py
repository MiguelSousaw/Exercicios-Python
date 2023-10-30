lula= 0 
bolsonaro= 0
ciro = 0
eleitores = int (input('Digite o número de eleitores: '))
for i in range (eleitores):
    voto = input (f"Digite o número (13/22/12) do candidato em que o eleitor {i+1} quer votar: ") 
    if voto == '13':
        lula +=  1
    if voto == '12':
         ciro += 1
    if voto ==  '22':
        bolsonaro += 1
print ('Votação Encerrada'
           
           f' CANDIDATO LULA  {lula }  VOTOS, '
            f' CANDIDATO BOLSONARO  {bolsonaro}  VOTOS, '
             f' CANDIDATO CIRO  {ciro}  VOTOS' )

print ('--='*20)
if lula > bolsonaro and lula > ciro:
    print ('O  NOVO PRESIDENTE DA REPÚBLICA É LUIS INACIO LULA DA SILVA')
elif bolsonaro > lula and bolsonaro > ciro:
    print ('O NOVO PRESIDENTE DA REPÚBLICA É JAIR MESSIAS BOLSONARO')
elif ciro > bolsonaro and ciro > lula:
    print ('O NOVO PRESIDENTE DA REPÚBLICA É CIRO FERREIRA GOMES')
else:
    print('EMPATE')

    