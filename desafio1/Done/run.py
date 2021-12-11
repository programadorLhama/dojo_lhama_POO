from components import Elevador

elevador = Elevador()

while (True):
    andar = int(input('Defina um andar: '))
    response = elevador.locomover(andar)
    print(response)
    print()
