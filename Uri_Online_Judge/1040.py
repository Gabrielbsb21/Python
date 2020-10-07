# programa feito com a versão 3.8 do Python

number_1, number_2, number_3, number_4 = input().split(' ')
number_1 = int(number_1)
number_2 = int(number_2)
number_3 = int(number_3)
number_4 = int(number_4)
media = (number_1 * 2 + number_2 * 3 + number_3 * 4 + number_4) / 10
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
elif media >= 5 or media <= 6.9:
    print('Aluno em exame.')
