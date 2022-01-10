from planejador_de_viajem import PlanejadorDeViajem
from destinos.belo_horizonte import BeloHorizonte
from destinos.fortaliza import Fortaleza
from destinos.niterio import Niteroi

planejadorDeViajem = PlanejadorDeViajem()

while (True):
    destino = None

    destino_da_viajem = input('Selecione o destino da viajem: ')
    if (destino_da_viajem == '1'): destino = Niteroi()
    elif (destino_da_viajem == '2'): destino = BeloHorizonte()
    elif (destino_da_viajem == '3'): destino = Fortaleza()

    atividade = planejadorDeViajem.viajar(destino)
    print(atividade)
    print()
