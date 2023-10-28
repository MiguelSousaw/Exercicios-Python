a = int (input('Digite a População do país A: '))
b = int (input('Digiite a População do país B: '))
taxaA = int (input('Agora, insira aqui a taxa de crescimento da população A por ano em porcentagem (sem adicionar o simbolo "%"): '))
taxaB = int (input('Agora, insira aqui a taxa de crescimento da população B por ano em porcentagem (sem adicionar o simbolo "%"): '))
anos = 0

while a < b:
    anos += 1
    a =  a + (a*(taxaA/100))
    b = b + (b*(taxaB/100))
    if a >= b: 
        print (f'Demorou {anos} anos para a população de "A" passar ou igualar a de "B".')
        print (f'"A" tem {a} habitantes  e "B" tem {b} habitantes')
        break