import sqlite3
from sqlite3 import Error


def create_connection(db_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print("Erro: ", e)

  return conn