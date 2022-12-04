from sqlite3 import Error


class Compra:

  def __init__(self, tituloLivro, preco, prioridade, comprado):
    self.tituloLivro = tituloLivro
    self.preco = preco
    self.prioridade = prioridade
    self.comprado = comprado

  def get_compra(conn):
    try:
      c = conn.cursor()
      c.execute("SELECT * FROM compra;")
      result = c.fetchall()
      type(result)
      return result
    except Error as e:
      return e

  def add_compra(self, conn):
    try:
      c = conn.cursor()
      compra = (self.tituloLivro, self.preco, self.prioridade, self.comprado)
      c.execute(
        "INSERT INTO compra (tituloLivro, preco, prioridade, comprado) VALUES (?, ?, ?, ?);",
        compra)
      conn.commit()
    except Error as e:
      return e

  def update_compra(conn, values):
    try:
      c = conn.cursor()
      c.execute(
        "UPDATE compra SET tituloLivro=?, preco=?, prioridade=?, comprado=? WHERE idCompra=?;",
        values)
      conn.commit()
    except Error as e:
      return e

  def deletar_compra(conn, id):
    try:
      c = conn.cursor()
      c.execute("DELETE FROM compra where idCompra=?;", id)
      conn.commit()
    except Error as e:
      return e
