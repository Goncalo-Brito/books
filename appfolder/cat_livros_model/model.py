from .. import db
from sqlalchemy.orm import relationship


class Rel(db.Model):
    id_cat = db.Column(db.Integer, db.ForeignKey("cats.id_cat"), primary_key=True)
    id_livro = db.Column(db.Integer, db.ForeignKey("livros.id_livro"), primary_key=True)
    catlink = relationship("Cats")

    def __init__(self, id_cat, id_livro):
        self.id_cat = id_cat
        self.id_livro = id_livro
