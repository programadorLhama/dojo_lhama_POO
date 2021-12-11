class GerenciadorDeJogo:
    def __init__(self, jogador1, jogador2) -> None:
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2
    
    def apostarRodada(self):
        jogador1_jogada = self.__jogador1.fazer_jogada()
        jogador2_jogada = self.__jogador2.fazer_jogada()

        resultado_da_rodada = self.__verificar_jogadas(jogador1_jogada, jogador2_jogada)

        if (resultado_da_rodada == 1): self.__jogador1.incrementar_vitorias()
        if (resultado_da_rodada == 2): self.__jogador2.incrementar_vitorias()

        return self.__apresentar_resultados()

    def __verificar_jogadas(self, jogador1_jogada, jogador2_jogada):
        if (jogador1_jogada == jogador2_jogada): return 0
        if (
            (jogador1_jogada == 'pedra' and jogador2_jogada == 'tesoura')
            or (jogador1_jogada == 'papel' and jogador2_jogada == 'pedra')
            or (jogador1_jogada == 'tesoura' and jogador2_jogada == 'papel')
        ): return 1
        else: return 2
    
    def __apresentar_resultados(self):
        return '{} --- {}'.format(
            self.__jogador1.apresentar_vitorias(),
            self.__jogador2.apresentar_vitorias()
        )