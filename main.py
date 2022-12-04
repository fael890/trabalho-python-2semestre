from model.db_tables import create_tables
from model.db_connection import create_connection
from view.menu_principal import menu

if __name__ == '__main__':
  conn = create_connection("livros.db")
  create_tables(conn)

  menu(conn)
