import random

class Livro:
    def __init__(self, titulo, autor, ano) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.id = random.randint(0, 1000000)