from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()  # estou instanciando o objeto

comodo = Comodo(
    input('Qual a largura do cômodo? '),
    input('Qual a profundidade do cômodo? ')
)

print(
    f'A area das paredes é: {calc.calcular_area_paredes(comodo)}')
print(
    f'A area do teto é: {calc.calcular_area_teto(comodo)}')
print(
    f'A litragem de tinta necessária é: {calc.calcular_litragem_necessaria()}')
