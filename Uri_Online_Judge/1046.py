hr1, hr2 = input().split(" ");
hr1 = int(hr1);
hr2 = int(hr2);
tempo = 24 - hr1 + hr2;
if(tempo > 24):
    tempo = tempo -24;
    print("O JOGO DUROU %d HORA(S)" %tempo);
else:
    print("O JOGO DUROU %d HORA(S)" %tempo);