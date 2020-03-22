a = 0;
qtd = 0;
media = 0;
for a in range(6):
    num = float(input());
    if(num > 0):
        qtd += 1;
        media += num;
media = media / qtd;
print("%d valores positivos" %qtd);
print("%.1f" %media);