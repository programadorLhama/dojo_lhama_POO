class Login:
    def __init__(self) -> None:
        self.__usuarios = []
    
    def adicionar_usuario(self, usuario, senha):
        cadastro = { "usuario": usuario, "senha": senha }
        self.__usuarios.append(cadastro)
    
    def logar_usuario(self, usuario, senha):
        cadastro = None

        for registro in self.__usuarios:
            if (registro["usuario"] == usuario and registro["senha"] == senha):
                cadastro = registro
                break
        
        return cadastro

login = Login()
