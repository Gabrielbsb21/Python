qtd_par = 0;
qtd_impar = 0;
qtd_positivo = 0;
qtd_negativo = 0;
for a in range(0, 5):
    num = int(input());
    if(num > 0):
        qtd_positivo += 1;
    elif(num < 0):
        qtd_negativo += 1;
    if(num % 2 == 0):
        qtd_par += 1;
    if(num % 2 != 0):
        qtd_impar += 1;


print("%d valor(es) par(es)" %qtd_par);
print("%d valor(es) par(es)" %qtd_impar);
print("%d valor(es) par(es)" %qtd_positivo);
print("%d valor(es) par(es)" %qtd_negativo);
