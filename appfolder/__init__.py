from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://estagio:estagio@localhost:5432/db_biblioteca'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .livros_model.model import *
from .cat_model.model import *
from .cat_livros_model.model import *


@app.route('/')
def my_form():
    return redirect(url_for('livros_form'))


@app.route('/livros')
def livros_form():
    template_data = {
        'livros': Livros.query.all(),
        'cat': Cats.query.all(),
        'rel': Rel.query.all()
    }
    print(dir(template_data['rel'][0]))
    print(template_data['rel'][0].catlink.nome_cat)
    return render_template('livros.html', data=template_data)


@app.route('/new_livro', methods=['GET', 'POST'])
def new_livro():
    if request.method == 'POST':
        if not request.form['nome_livro'] or not request.form['autor'] or not request.form['classi'] or request.form.getlist('cat') == 0:
            flash('Please enter all the fields', 'error')
        else:
            livro = Livros(request.form['nome_livro'], request.form['autor'], request.form['classi'])
            db.session.add(livro)
            db.session.commit()
            # print("Cat ", request.form.getlist('cat'))
            cats = request.form.getlist('cat')
            for mycat in cats:
                tmprel = Rel(mycat, livro.id_livro)
                db.session.add(tmprel)
                db.session.commit()

            flash('Record was successfully added')
            return redirect(url_for('livros_form'))

    template_data = {
        'categorias': Cats.query.all()
    }

    return render_template('new_livro.html', data=template_data)


@app.route('/delete_livro/<int:id_livro>', methods=['GET'])
def delete_livro(id_livro):
    rel = Rel.query.filter(Rel.id_livro == id_livro).delete()
    if(rel > 0):
        db.session.commit()
    lines = Livros.query.filter(Livros.id_livro == id_livro).delete()
    if(lines > 0):
        db.session.commit()
        flash('Mensagem apagada com sucesso')
    else:
        flash('O id do registo nao existe')
    return redirect(url_for('livros_form'))


@app.route('/update_livro/<int:id_livro>', methods=['GET', 'POST'])
def update_livro(id_livro):
    livroupdate = Livros.query.get_or_404(id_livro)
    if request.method == 'POST':
        if not request.form['nome_livro'] or not request.form['autor'] or not request.form['classi'] or request.form.getlist('cat') == 0:
            flash('Please enter all the fields', 'error')
        else:
            rel = Rel.query.filter(Rel.id_livro == id_livro).delete()
            if(rel > 0):
                db.session.commit()
            cats = request.form.getlist('cat')
            livroupdate.nome_livro = request.form['nome_livro']
            livroupdate.autor = request.form['autor']
            livroupdate.classi = request.form['classi']
            db.session.add(livroupdate)
            db.session.commit()
            for mycat in cats:
                tmprel = Rel(mycat, livroupdate.id_livro)
                db.session.add(tmprel)
                db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('livros_form'))
    template_data = {
        'category': livroupdate,
        'categorias': Cats.query.all()
    }
    return render_template('livros_update.html', data=template_data)


@app.route('/categorias')
def cat_form():
    template_data = {
        'cats': Cats.query.all()
    }
    return render_template('cat.html', data=template_data)


@app.route('/new_cat', methods=['GET', 'POST'])
def new_cat():
    if request.method == 'POST':
        if not request.form['nome_cat']:
            flash('Please enter all the fields', 'error')
        else:
            cat = Cats(request.form['nome_cat'])
            print(cat.id_cat)
            db.session.add(cat)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('cat_form'))
    return render_template('new_cat.html')


@app.route('/delete_cat/<int:id_cat>', methods=['GET'])
def delete_cat(id_cat):
    lines = Cats.query.filter(Cats.id_cat == id_cat).delete()
    if(lines > 0):
        db.session.commit()
        flash('Mensagem apagada com sucesso')
    else:
        flash('O id do registo nao existe')
    return redirect(url_for('cat_form'))


@app.route('/update_cat/<int:id_cat>', methods=['GET', 'POST'])
def update_cat(id_cat):
    catupdate = Cats.query.get_or_404(id_cat)
    if request.method == 'POST':
        if not request.form['nome_cat']:
            flash('Please enter all the fields', 'error')
        else:
            catupdate.nome_cat = request.form['nome_cat']
            db.session.add(catupdate)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('cat_form'))
    template_data = {
        'category': catupdate
    }
    return render_template('cat_update.html', data=template_data)


@app.route('/teste')
def teste():
    return render_template('sidebar_site2.html')
