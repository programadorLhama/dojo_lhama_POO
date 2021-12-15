from model import RepositorioDeLivros

repositorioDeLivros = RepositorioDeLivros()

while (True):
    escolha = input('1 - Cadastrar livro / 2 - listar livros: ')
    if (escolha == '1'):
        titulo = input('Defina Titulo do Livro: ')
        autor = input('Defina Autor do Livro: ')
        ano = input('Defina Ano do Livro: ')
        repositorioDeLivros.registrar_livro(titulo, autor, ano)
    
    if (escolha == '2'):
        repositorioDeLivros.listar_livros()

