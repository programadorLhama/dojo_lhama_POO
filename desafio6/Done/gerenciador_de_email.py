class GerenciadorDeEmail:
    def __init__(self, nome_remetente, email_remetente) -> None:
        self.__nome_remetente = nome_remetente
        self.__email_remetente = email_remetente
        self.__assunto = None
        self.__mensagem = None
        self.__lista_destinatarios = []
    
    def criar_email (self, assunto, mensagem):
        self.__assunto = assunto
        self.__mensagem = mensagem
    
    def adicionar_destinatario (self, destinatario):
        self.__lista_destinatarios.append(destinatario)
    
    def enviar_email (self):
        print(
            '''
            Enviando mensagem:
            Remetente: {}
            Email: {}
            - {}
            : {}
            '''.format(
                self.__nome_remetente,
                self.__email_remetente,
                self.__assunto,
                self.__mensagem
            )
        )

        print('Destinatarios:')
        for destinatario in self.__lista_destinatarios:
            print('     {} - {}'.format(destinatario.nome, destinatario.email))

        
