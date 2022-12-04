import view.menu_livro as menuLivro
import view.menu_rotulo as menuRotulo
import view.menu_compra as menuCompra
from terminal_clear import clear
from cores import Cores


#Menu
def menu(conn):
  opcao = None
  while opcao != 0:
    print('*' * 30)
    print(f"{Cores.TEXTO}1 - Menu de livros{Cores.FIM}")
    print(f"{Cores.TEXTO}2 - Menu de rotulos{Cores.FIM}")
    print(f"{Cores.TEXTO}3 - Menu de compras futuras{Cores.FIM}")
    print('*' * 30)
    print(f"{Cores.AVISO}0 - SAIR{Cores.FIM}")
    print('*' * 30)
    opcao = int(input(f"{Cores.INPUT}Digite a opção que deseja: {Cores.FIM}"))
    clear()

    if opcao == 1:
      menuLivro.submenu(conn)
    if opcao == 2:
      menuRotulo.submenu(conn)
    if opcao == 3:
      menuCompra.submenu(conn)
