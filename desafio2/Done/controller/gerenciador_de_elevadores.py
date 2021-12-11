class GerenciadorDeElevadores:
    def __init__(self, elevador1, elevador2) -> None:
        self.__elevadores = [elevador1, elevador2]
    
    def locomover(self, andar, id):
        if (andar < 1 or andar > 15): return self.__mensagem_de_erro()
        else: return self.__filtrar_elevador_e_alterar_andar(andar, id)
    
    def __filtrar_elevador_e_alterar_andar(self, andar, id):
        for elevador in self.__elevadores:
            if elevador.check_id(id):
                return self.__alterar_andar_e_retornar_informacao(andar, elevador)
        
        return self.__mensagem_de_erro_de_elevador()

    def __alterar_andar_e_retornar_informacao(self, andar, elevador):
        elevador.set_andar(andar)
        if (andar == 1): return self.__mensagem_de_alteracao_para_terreo(elevador)
        return self.__mensagem_de_alteracao_de_andar(elevador)

    def __mensagem_de_erro(self):
        return 'Andar incorreto!'
    
    def __mensagem_de_alteracao_de_andar(self, elevador):
        return 'Elevador {} indo para o {}° andar'.format(elevador.get_id(), elevador.get_andar())
    
    def __mensagem_de_alteracao_para_terreo(self, elevador):
        return 'Elevador {} indo para o terreo'.format(elevador.get_id())
    
    def __mensagem_de_erro_de_elevador(self):
        return 'Elevador nao existe'
