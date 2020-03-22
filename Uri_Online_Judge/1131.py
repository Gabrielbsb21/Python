val = 3;
grenais = 0;
empates = 0;
inter = 0;
gremio = 0;
while val != 2:
 gol1, gol2 = input(). split(" ");
 gol1 = int(gol1);
 gol2 = int(gol2);
 grenais +=1;
 if gol1 > gol2:
   inter += 1;
 elif gol1 < gol2:
    gremio += 1;
 elif gol1 == gol2:
   empates += 1;
 val = int(input("Novo grenal (1-sim 2-nao)\n"));
if inter > gremio:
  print("%d grenais" %grenais);
  print("Inter:%d" %inter);
  print("Gremio:%d" %gremio);
  print("Empates:%d" %empates);
  print("Inter venceu mais");
else:
  print("%d grenais" %grenais);
  print("Inter:%d" %inter);
  print("Gremio:%d" %gremio);
  print("Empates:%d" %empates);
  print("Gremio venceu mais");
