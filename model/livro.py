from sqlite3 import Error


class Livro:

  def __init__(self, nomeLivro, lido):
    self.nomeLivro = nomeLivro
    self.lido = lido

  def get_livro(conn):
    try:
      c = conn.cursor()
      c.execute("SELECT * FROM livro;")
      result = c.fetchall()
      type(result)
      return result
    except Error as e:
      return e

  def add_livro(self, conn):
    try:
      c = conn.cursor()
      livro = (self.nomeLivro, self.lido)
      c.execute("INSERT INTO livro (nomeLivro, lido) VALUES (?, ?);", livro)
      conn.commit()
    except Error as e:
      return e

  def update_livro(conn, values):
    try:
      c = conn.cursor()
      c.execute("UPDATE livro SET nomeLivro=?, lido=? where idLivro=?", values)
      conn.commit()
    except Error as e:
      return e

  def lido_livro(conn, id, lido):
    try:
      c = conn.cursor()
      c.execute("UPDATE livro SET lido=? WHERE idLivro=?", (lido, id))
      conn.commit()
    except Error as e:
      return e

  def deletar_livro(conn, id):
    try:
      c = conn.cursor()
      c.execute("DELETE FROM livro WHERE idLivro=?", id)
      conn.commit()
    except Error as e:
      return e

  def grafico_categoria_livro(conn):
    categorias = []
    contagemCategorias = []
    try:
      c = conn.cursor()
      c.execute(
        "SELECT categoria, count(categoria) FROM rotulo group by categoria")
      contagemLivro = c.fetchall()

      for i in range(len(contagemLivro)):
        categorias.append(contagemLivro[i][0])
        contagemCategorias.append(contagemLivro[i][1])

      return (categorias, contagemCategorias)
    except Error as e:
      return e

  def exibir_rotulo_livro(conn):
    try:
      c = conn.cursor()
      c.execute(
        "SELECT l.*, r.* FROM rotulo r INNER JOIN livro l ON l.idLivro = r.idLivro"
      )
      result = c.fetchall()
      return result
    except Error as e:
      return e
