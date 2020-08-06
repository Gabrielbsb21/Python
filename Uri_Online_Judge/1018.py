# programa feito com a versão 3.8 do Python

number = int(input())
aux = number
hundred = int(number / 100)
number = number - hundred * 100  
cinquenta = int(number / 50)
number = number - cinquenta * 50 
vinte = int(number / 20)
number = number - vinte * 20 
dez = int(number / 10)
number = number - dez * 10 
cinco = int(number / 5)
number = number - cinco * 5 
dois = int(number / 2)
number = number - dois * 2 
print(aux)
print(f'{hundred} notas(s) de R$ 100,00')
print(f'{cinquenta} notas(s) de R$ 50,00')
print(f'{vinte} notas(s) de R$ 20,00' )
print(f'{dez} notas(s) de R$ 10,00' )
print(f'{cinco} notas(s) de R$ 5,00' )
print(f'{dois} notas(s) de R$ 2,00')
print(f'{number} notas(s) de R$ 1,00')