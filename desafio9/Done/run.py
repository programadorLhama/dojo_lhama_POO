from login import login
from texto_secreto import texto_secreto
from gerenciador_de_login import GerenciadorDeLogin

gerenciador_de_login = GerenciadorDeLogin(login, texto_secreto)
usuario = 'rafael'
senha = 'minhaSenha'

login.adicionar_usuario(usuario, senha)

gerenciador_de_login.logar_usuario(usuario, senha)

