from gerenciador_de_email import GerenciadorDeEmail
from destinatario import Destinatario

gerenciadorDeEmail = GerenciadorDeEmail('Rafa Ferreira', 'rafa@email.com')

while True:
    assunto = input('Defina o Titulo do Email: ')
    mensagem = input('Defina o assunto: ')
    print()

    gerenciadorDeEmail.criar_email(assunto, mensagem)

    command = 's'
    while command == 's':
        nome = input('Defina o nome do Destinatario: ')
        email = input('Defina o email do Destinatario: ')
        destinatario = Destinatario(nome, email)
        gerenciadorDeEmail.adicionar_destinatario(destinatario)
        print()

        command = input('Deseja adicionar outro destinatario ?: ')

    gerenciadorDeEmail.enviar_email()
    print()
