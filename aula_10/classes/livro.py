class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
    
    def __str__(self):
        return f"'{self.titulo}' de {self.autor}"