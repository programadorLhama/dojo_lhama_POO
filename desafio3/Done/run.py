from model import Jogador
from controller import GerenciadorDeJogo

jogador1 = Jogador('Joaozinho')
jogador2 = Jogador('Pedrinho')
gerenciadorDeJogo = GerenciadorDeJogo(jogador1, jogador2)

while (True):
    input()
    resultado = gerenciadorDeJogo.apostarRodada()
    print(resultado)
