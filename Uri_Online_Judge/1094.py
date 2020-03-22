num = int(input());
total_coelhos = 0;
total_ratos = 0;
total_sapos = 0;
for _ in range(num):
    a, b = input(). split(" ");
    a = int(a);
    b = str(b);
    if b == 'C':
        total_coelhos = a + total_coelhos;
    elif b == 'R':
        total_ratos = a + total_ratos;
    elif b == 'S':
        total_sapos = a + total_sapos;
total = total_coelhos + total_ratos + total_sapos;
perc_coelho = (total_coelhos / total) * 100;
perc_ratos = (total_ratos / total) * 100;
perc_sapos = (total_sapos / total) * 100;
print("Total:",total, "cobaias");
print("Total de coelhos:",total_coelhos);
print("Total de ratos:",total_ratos);
print("Total de sapos:",total_sapos);
print("Percentual de coelhos: %.2f %%" %perc_coelho);
print("Percentual de ratos: %.2f %%" %perc_ratos);
print("Percentual de sapos: %.2f %%" %perc_sapos);

    
