class Elevador:
    def __init__(self) -> None:
        self.__andar = 1
    
    def locomover(self, andar):
        if (andar < 1 or andar > 15): return self.__mensagem_de_erro()
        else: return self.__alterar_andar_e_retornar_informacao(andar)
    
    def __alterar_andar_e_retornar_informacao(self, andar):
        self.__andar = andar
        if (andar == 1): return self.__mensagem_de_alteracao_para_terreo()
        return self.__mensagem_de_alteracao_de_andar()

    def __mensagem_de_erro(self):
        return 'Andar incorreto! Elevador no {}° andar'.format(self.__andar)
    
    def __mensagem_de_alteracao_de_andar(self):
        return 'Elevador indo para o {}° andar'.format(self.__andar)
    
    def __mensagem_de_alteracao_para_terreo(self):
        return 'Elevador indo para o terreo'
