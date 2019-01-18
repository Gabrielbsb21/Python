coord_1, coord_2 = 2, 2
while(coord_1 != 0 and coord_2 != 0):
    if(coord_1 != 0 and coord_2 != 0):
        coord_1, coord_2 = input().split(" ")
        coord_1 = int(coord_1)
        coord_2 = int(coord_2)
        if(coord_1 > 0 and coord_2 > 0):
            print("primeiro")
        elif(coord_1 > 0 and coord_2 < 0):
            print("quarto")
        elif(coord_1 < 0 and coord_2 > 0):
            print("segundo")
        elif(coord_1 <0 and coord_2 < 0):
            print("terceiro")
        