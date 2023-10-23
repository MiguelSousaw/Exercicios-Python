maçãs = float (input('Quantos quilos de maçãs foram compradas'))
morango = float (input('quantos quilos de morango foram comprados'))
valor = 0

if morango <= 5:
   valor = morango * 2.50 
else:
   valor = morango * 2.20 

if maçãs <= 5: 
   valor = maçãs * 1.80
else:
   valor = morango * 1.5

if morango + maçãs == 8 or valor > 25:
    valor -= valor * (10/100)

print(f"O valor a ser pago é R${valor:.2f}")