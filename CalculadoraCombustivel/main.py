from calculo import Calculo


def main():
    print("""
            Esta aplicação tem como finalidade demonstrar os valores que serão gastos com combustível durante a viagem,
            com base no consumo do seu veículo, e com a distância e o preço do combustível determinado por você!""")

    print("Os combustíveis disponíveis para este cálculo são:")
    print("º Gasolina")
    print("° Álcool")
    print("° Díesel")

    try:
        tipo_combustivel = input(
            "Digite o tipo de combutível que seu carro usa\n")
        preco_combustivel = float(
            input("Digite o preço do combustível que seu automovel usa\n"))
        distancia = float(input("Distância em Quilômetros a ser pecorrida\n"))
        consumo = float(input("Consumo de combustível do veículo (km/l)\n"))
        calculo = Calculo(preco_combustivel, tipo_combustivel)
        print(calculo.gasto_combustivel(distancia, consumo))

    except ValueError as erro:
        print("O valor recebido não é válido")


if __name__ == "__main__":
    main()
