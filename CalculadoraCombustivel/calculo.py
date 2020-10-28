class Calculo():
    def __init__(self, preco_combustivel, tipo_combustivel):
        self.__preco_combustivel = preco_combustivel
        self.__tipo_combustivel = tipo_combustivel

    def gasto_combustivel(self, distancia, consumo):
        if distancia <= 0 or consumo <= 0:
            raise Exception(
                "O valor recebido não pode ser menor ou igual a zero")

        gasto_total = round(
            (distancia / consumo) * self.__preco_combustivel, 2)

        return f""" O valor total gasto com a {self.__tipo_combustivel} será de:{gasto_total}"""
