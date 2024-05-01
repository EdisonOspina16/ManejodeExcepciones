from tiendalibros.modelo.libro import Libro


class LibroError(Exception):
    def __init__(self, libro: Libro):
        self.libro = libro
        
class LibroExistenteError(LibroError):
    def __init__(self, titulo, isbn):
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn

    def __str__(self):
        return f"El libro con titulo {self.titulo} y isbn: {self.isbn} ya existe en el catálogo"