create table categoria(
    id_categoria serial,
    nome_categoria varchar(32),
    primary key(id_categoria)
);

create table livro (
    id_livro serial,
    nome_livro varchar(64) not null unique,
    id_categoria int not null,
    autor varchar(32) not null,
    classi float(1) not null,
    primary key(id_livro), 
);

create table rel (
    id_livro int not null
    id_categoria int not null
    foreign key(id_livro) references livro(id_livro)
    foreign key(id_categoria) references categoria(id_categoria)
    primary key(id_livro, id_categoria)
);