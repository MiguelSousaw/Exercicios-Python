altura_mais_alto = 0
aluno_alto = 0
altura_mais_baixo = 200
aluno_baixo= 0
for c in range (1,11):
    altura = int(input(f'Digite a altura do aluno {c} em cm: '))
    if altura > altura_mais_alto: 
        aluno_mais_alto = c
        altura_mais_alto = altura
    if altura < altura_mais_baixo:
        aluno_baixo = c
        altura_mais_baixo = altura
print(f"O mais alto é o aluno {aluno_mais_alto} com {altura_mais_alto}cm")
print(f"O mais baixo é o aluno {aluno_baixo} com {altura_mais_baixo}cm")