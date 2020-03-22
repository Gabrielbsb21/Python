#creio que esta não é a forma mais elegante, porém se eu pensar em uma forma mais apresentalvel, corrigo o código
codigo = 1
gasolina = 0
alcool = 0
diesel = 0
while(codigo >= 1 and codigo <= 3):
    codigo = int(input())
    while(codigo < 1 or codigo > 5):
        codigo = int(input())
    if(codigo == 1):
        alcool = 1 + alcool
    elif(codigo == 2):
        gasolina = gasolina + 1
    elif(codigo == 3):
        diesel = diesel + 1
    if(codigo == 4):
        print("MUITO OBRIGADO")
        print(f'Alcool: {alcool}')
        print(f'Gasolina: {gasolina}')
        print(f'Diesel: {diesel}')


