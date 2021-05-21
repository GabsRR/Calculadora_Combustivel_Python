from calculo import Calculo

def main():
    print(
        """
        Calculadora de consumo de combustível que demonstra os valores necessários para realizar um deslocamento de 
        acordo com a distância a ser percorrida e o rendimento do veículo inseridos pelo usuário. Os valores serão
        mostrados para os combustíveis: Gasolina, Álcool e Diesel.
        """
    )

    try:
        distancia = float(input('Digite a distância a ser percorrida em Km: '))
        rendimento = float(input('Rendimento do véiculo em Km/L: '))
        calculo = Calculo()
        print(
            calculo.calcular_gasto(distancia, rendimento)
        )
    except ValueError as erro:
        print("Valor informado não é válido")


if __name__ == "__main__":
    main()