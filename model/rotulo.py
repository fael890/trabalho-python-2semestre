from sqlite3 import Error


class Rotulo:

  def __init__(self, numPags, preco, categoria, sinopse, autor, ano, idLivro):
    self.numPags = numPags
    self.preco = preco
    self.categoria = categoria
    self.sinopse = sinopse
    self.autor = autor
    self.ano = ano
    self.idLivro = idLivro

  def get_rotulo(conn):
    try:
      c = conn.cursor()
      c.execute("SELECT * FROM rotulo;")
      result = c.fetchall()
      return result
    except Error as e:
      return e

  def add_rotulo(self, conn):
    try:
      c = conn.cursor()
      rotulo = (self.numPags, self.preco, self.categoria, self.sinopse,
                self.autor, self.ano, self.idLivro)
      c.execute(
        "INSERT INTO rotulo (numPags, preco, categoria, sinopse, autor, ano, idLivro) VALUES (?, ?, ?, ?, ?, ?, ?);",
        rotulo)
      conn.commit()
    except Error as e:
      return e

  def update_rotulo(conn, values):
    try:
      c = conn.cursor()
      c.execute(
        "UPDATE rotulo SET numPags=?, descricao=?, preco=?, categoria=?, sinopse=?, editora=?, autor=?, ano=?, idioma=? WHERE idRotulo=?;",
        values)
      conn.commit()
    except Error as e:
      return e

  def deletar_rotulo(conn, id):
    try:
      c = conn.cursor()
      c.execute("DELETE FROM rotulo where idRotulo=?;", id)
      conn.commit()
    except Error as e:
      return e
