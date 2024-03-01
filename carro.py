from entidade.veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, modelo, cor, ano, num_portas, qtd_passageiros, tipo_combustivel, motorizacao):
        super().__init__(modelo, cor, ano)
        self.__num_portas = num_portas
        self.__qtd_passageiros = qtd_passageiros
        self.__tipo_combustivel = tipo_combustivel
        self.__motorizacao = motorizacao

    def exibir_informacao(self):
        super().exibir_conteudo()
        print(f"Número de Portas: {self.__num_portas}")
        print(f"Número de Passageiros: {self.__qtd_passageiros}")
        print(f"Tipo de Combustível: {self.__tipo_combustivel}")
        print(f"Tipo de Motor: {self.__motorizacao}")

    def calcular_km_plitro(self):
        if self.__motorizacao == "Mil":
            if self.__tipo_combustivel == "Etanol":
                return "12 km/l"
            elif self.__tipo_combustivel == "Gasolina":
                return "16 km/l"

        elif self.__motorizacao == "1.6":
            if self.__tipo_combustivel == "Etanol":
                return "11 km/l"
            elif self.__tipo_combustivel == "Gasolina":
                return "14 km/l"

        elif self.__motorizacao == "1.8":
            if self.__tipo_combustivel == "Etanol":
                return "10 km/l"
            elif self.__tipo_combustivel == "Gasolina":
                return "12 km/l"

        elif self.__motorizacao == "2.0":
            if self.__tipo_combustivel == "Etanol":
                return 8
            elif self.__tipo_combustivel == "Gasolina":
                return 10

        else:
            return 0
