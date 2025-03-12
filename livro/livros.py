class Livro:
    def __init__(self, nome, autor, genero, editora, paginas):
        self.nome = nome
        self.__autor = autor
        self.genero = genero
        self.editora = editora
        self.paginas = paginas

    def __str__(self):
        return f"O livro {self.nome} foi escrito por { self.__autor}, é do genero {self.genero}, publicado pela editora {self.editora} e tem {self.paginas} paginas"