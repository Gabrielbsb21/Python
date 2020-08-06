# programa feito com a versão 3.8 do Python

age = int(input())
year = int(age / 365)
age = age - year * 365
month = int(age / 30)
days = age - month * 30
print(f'{year} ano(s)')
print(f'{month} mes(es)')
print(f'{days} dia(s)')
