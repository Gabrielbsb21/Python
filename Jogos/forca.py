#coding: utf-8
# jogo da forca

# funcoes que vou fazer para o codigo nao ficar tao bagunçado


def inicial():
    a = '-'
    print("BEM-VINDO AO LADO NEGRO DA FORÇA")
    print("ESSE VAI SER O JOGO DA FORCA, QUE VENÇA O MELHOR!!!")
    print(33 * a)
    print("""Intruções: 
    1- O jogo vai ser composto de dois jogadores.
    2- O jogador_1 vai gravar a palavra a ser descoberta, e o jogador_2 vai tentar descobrir.
    3- O jogador_1 vai poder dar uma dica sobre a palavra.
    4- Se o jogador_2 errar três vezes, a dica vai aparecer se o jogador_1 deu alguma dica, senão vai aparecer 
    uma mensagem que não foi informado nenhuma dica
    5- O jogo acaba quando o jogador_2 acertar a palavra ou morrer na forca""")
    print()


'''------------------
parte principal do código'''

inicial()
print("Digite a palavra secreta, por favor")
palavra_secreta = input()
print()  # para pular uma linha
print("Deseja dar uma dica para a palavra secreta?! Se sim, digite 1, caso contrario digite 2")
num = int(input())
if(num == 1):
    print("Digite a dica:")
    dica = input()
elif(num == 2):
    print("Vamos prosseguir o jogo sem dica :(\n")

print("VAMOS COMEÇAR\n")
print("DIGITE UMA LETRA, POR FAVOR")

letra = input()


