from entidade.carro import Carro


if __name__ == '__main__':
    carro = Carro("Mustang", "Branco", "1967","2","4","Gasolina","V8 2.0")
    carro.exibir_informacao()
    print(carro.calcular_km_plitro())

