from .. import db
#from sqlalchemy.orm import relationship


class Cats(db.Model):
    id_cat = db.Column('id_cat', db.Integer, primary_key=True)
    nome_cat = db.Column(db.String(64))

    def __init__(self, nome_cat):
        self.nome_cat = nome_cat
