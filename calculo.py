class Calculo:
    def __init__(self):
        self.__valor_gasolina = 5.35
        self.__valor_alcool = 4.80
        self.__valor_diesel = 5.00

    def calcular_gasto(self, distancia, rendimento):
        if distancia <= 0 or rendimento <= 0:
            raise Exception('o valor informado de distância ou de rendimento não pode ser igual a zero!')

        gasto_gasolina = round(
            (distancia / rendimento) * self.__valor_gasolina, 2)

        gasto_alcool = round(
            (distancia / rendimento) * self.__valor_alcool, 2)

        gasto_diesel = round(
            (distancia / rendimento) * self.__valor_diesel, 2)

        return """
        O valor necessário será:
            Gasolina: R${}
            Álcool: R${}
            Diesel: R${}
        """.format(
            gasto_gasolina, gasto_alcool, gasto_diesel
        )