from model.compra import Compra
from terminal_clear import clear
from cores import Cores


def exibir_compra(conn):
  values = Compra.get_compra(conn)
  if values != []:
    for i in range(len(values)):
      comprado = "Sim" if values[i][4] == 1 else "Não"
      print(f"{Cores.TEXTO}ID: {Cores.FIM} {values[i][0]}")
      print(f"{Cores.TEXTO}Nome: {Cores.FIM} {values[i][1]}")
      print(f"{Cores.TEXTO}Preco: {Cores.FIM} {values[i][2]}")
      print(f"{Cores.TEXTO}Prioridade: {Cores.FIM} {values[i][3]}")
      print(f"{Cores.TEXTO}Comprado: {Cores.FIM} {comprado}")
  else:
    print(f"\n{Cores.AVISO}Não existe compras cadastrados!!!{Cores.FIM}")


def inserir_compra(conn):
  tituloCompra = input("Digite o título : ")
  precoCompra = input("Digite o novo preço: ")
  prioridadeCompra = input("Digite a prioridade da compra: ")
  comprado = input("Esse livro já foi comprado? \n 1 - Sim \n 0 - Não ")
  if comprado < '0' or comprado > '1':
    print("Valor inválido!!!")
    input("\nPressione <ENTER> para continuar ...")
    clear()
    submenu(conn)

  compra = Compra(tituloCompra, precoCompra, prioridadeCompra, comprado)
  result = compra.add_compra(conn)
  if result != None:
    print(result)
  else:
    print(f"\n{Cores.SUCESSO}Compra inserida com sucesso!!!{Cores.FIM}")


def atualizar_compra(conn):
  tituloCompra = input("Digite o título : ")
  precoCompra = input("Digite o novo preço: ")
  prioridadeCompra = input("Digite a prioridade da compra: ")
  comprado = input("Esse livro já foi comprado? \n 1 - Sim \n 0 - Não ")
  if comprado < '0' or comprado > '1':
    print("Valor inválido!!!")
    submenu()
    input("\nPressione <ENTER> para continuar ...")
    clear()
  values = (tituloCompra, precoCompra, prioridadeCompra, comprado)
  result = Compra.update_compra(conn, values)
  if result != None:
    print(result)
  else:
    print(f"\n{Cores.SUCESSO}Compra atualizada com sucesso!!!{Cores.FIM}")


def deletar_compra(conn):
  id = input("Digite o ID que deseja deletar: ")
  result = Compra.deletar_compra(conn, id)
  if result != None:
    print(result)
  else:
    print(f"\n{Cores.SUCESSO}Compra deletado com sucesso!!!{Cores.FIM}")


def submenu(conn):
  opcao_sub = None
  while opcao_sub != 0:
    print('*' * 30)
    print(f"{Cores.TEXTO}1 - Exibir futuras compras{Cores.FIM}")
    print(f"{Cores.TEXTO}2 - Inserir futura compra{Cores.FIM}")
    print(f"{Cores.TEXTO}3 - Atualizar futura compra{Cores.FIM}")
    print(f"{Cores.TEXTO}4 - Deletar futura compra{Cores.FIM}")
    print('*' * 30)
    print(f"{Cores.AVISO}0 - SAIR{Cores.FIM}")
    print('*' * 30)
    opcao_sub = int(input(f"{Cores.INPUT}Digite a opção: {Cores.FIM}"))
    clear()

    if opcao_sub == 1:
      exibir_compra(conn)

    if opcao_sub == 2:
      inserir_compra(conn)

    if opcao_sub == 3:
      atualizar_compra(conn)

    if opcao_sub == 4:
      deletar_compra(conn)

    input(f"\n{Cores.INPUT}Pressione <ENTER> para continuar ...{Cores.FIM}")
    clear()
