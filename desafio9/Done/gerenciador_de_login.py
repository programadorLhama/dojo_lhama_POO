class GerenciadorDeLogin:
    def __init__(self, login, texto_secreto) -> None:
        self.__login = login
        self.__texto_secreto = texto_secreto
    
    def logar_usuario(self, usuario, senha):
        self.__checar_cadastro_de_usuario(usuario, senha)
        self.__texto_secreto.apresentar_texto()
        pass

    def __checar_cadastro_de_usuario(self, usuario, senha):
        cadastro = self.__login.logar_usuario(usuario, senha)
        if not cadastro: raise Exception()

