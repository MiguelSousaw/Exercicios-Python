from time import sleep 
sleep (2)
while True: 
    print ('-='*20)
    print ('LOJA TABAJARA')
    print ('-='*20)
    produto = 0
    soma = 0
    cont = 0
    print  ('[DIGITE 999 PARA ENCERRAR]')
    print ('-='*20)
    while produto != 999:
        cont += 1
        produto = float (input(f'Produto {cont}: R$'))
        soma += produto 
    preço = soma 
    print (f'O preço total dos produtos comprados é de R${preço}')
    dinheiro = float (input('Quanto do seu dinheiro será entregue para pagamento? R$'))
    troco = dinheiro - preço 
    print (f'Seu troco é de R${troco}')
    sleep (2)
