from .. import db
#from sqlalchemy.orm import relationship


class Livros(db.Model):
    id_livro = db.Column('id_livro', db.Integer, primary_key=True)
    nome_livro = db.Column(db.String(128))
    autor = db.Column(db.String(64))
    classi = db.Column(db.Float())

    def __init__(self, nome_livro, autor, classi):
        self.nome_livro = nome_livro
        self.autor = autor
        self.classi = classi
