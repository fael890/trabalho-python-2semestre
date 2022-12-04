from sqlite3 import Error


def create_tables(conn):
  try:
    c = conn.cursor()
    
    c.execute('''
      CREATE TABLE IF NOT EXISTS rotulo(
        idRotulo integer not null primary key autoincrement,
        numPags integer,
        preco real,
        categoria text,
        sinopse text,
        autor text,
        ano integer,
        idLivro integer,
        foreign key(idLivro) references livro(idLivro)
      );
    ''')

    c.execute(''' 
      CREATE TABLE IF NOT EXISTS livro(
        idLivro integer not null primary key autoincrement,
        nomeLivro text,
        lido numeric
      );
    ''')

    c.execute('''
      CREATE TABLE IF NOT EXISTS compra(
        idCompra integer not null primary key autoincrement,
        tituloLivro text,
        preco real,
        prioridade integer,
        comprado integer
      );
    ''')

  except Error as e:
    print("Erro: ", e)
