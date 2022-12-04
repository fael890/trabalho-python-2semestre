from model.rotulo import Rotulo
from terminal_clear import clear
from cores import Cores


def exibir_rotulo(conn):
  values = Rotulo.get_rotulo(conn)
  if values != []:
    for i in range(len(values)):
      print(f"{Cores.TEXTO}ID: {Cores.FIM} {values[i][0]} ")
      print(f"{Cores.TEXTO}Nº Pags: {Cores.FIM} {values[i][1]} ")
      print(f"{Cores.TEXTO}Preco: {Cores.FIM} {values[i][2]} ")
      print(f"{Cores.TEXTO}Categoria: {Cores.FIM} {values[i][3]} ")
      print(f"{Cores.TEXTO}Sinopse: {Cores.FIM} {values[i][4]} ")
      print(f"{Cores.TEXTO}Autor: {Cores.FIM} {values[i][5]} ")
      print(f"{Cores.TEXTO}Ano: {Cores.FIM} {values[i][6]} ")
      print(f"{Cores.TEXTO}ID do Livro: {Cores.FIM} {values[i][7]}\n\n")
  else:
    print(f"{Cores.AVISO}Não existe rotulos cadastrados!!!{Cores.FIM}")


def inserir_rotulo(conn):
  numPags = input("Digite o número de páginas do livro: ")
  preco = input("Digite o preço do livro: ")
  categoria = input("Digite a categoria do livro: ")
  sinopse = input("Digite a sinopse do livro: ")
  autor = input("Digite o autor do livro: ")
  ano = input("Digite o ano do livro: ")
  idLivro = input("Digite o id do livro que esse rotulo pertence: ")

  rot = Rotulo(numPags, preco, categoria, sinopse, autor, ano, idLivro)

  result = rot.add_rotulo(conn)
  if result != None:
    print(result)
  else:
    print(f"\n{Cores.SUCESSO}Rotulo inserido com sucesso!!!{Cores.FIM}")


def atualizar_rotulo(conn):
  numPags = input("Digite a nova número de páginas: ")
  preco = input("Digite a nova preço: ")
  categoria = input("Digite a nova categoria: ")
  sinopse = input("Digite a nova sinopse: ")
  autor = input("Digite a nova autor: ")
  ano = input("Digite a nova ano: ")

  values = (numPags, preco, categoria, sinopse, autor, ano)
  result = Rotulo.update_rotulo(conn, values)
  if result != None:
    print(result)
  else:
    print(f"\n{Cores.SUCESSO}Rotulo atualizado com sucesso!!!{Cores.FIM}")


def deletar_rotulo(conn):
  id = tuple(input("Digite o ID que deseja deletar: "))
  print(type(id))
  result = Rotulo.deletar_rotulo(conn, id)
  if result != None:
    print(result)
  else:
    print(f"\n{Cores.SUCESSO}Rotulo deletado com sucesso!!!{Cores.FIM}")


#submenu
def submenu(conn):
  opcao_sub = None
  while opcao_sub != 0:
    print('*' * 30)
    print(f"{Cores.TEXTO}1 - Exibir rotulos dos livros{Cores.FIM}")
    print(f"{Cores.TEXTO}2 - Inserir rotulo no livro{Cores.FIM}")
    print(f"{Cores.TEXTO}3 - Atualizar rotulo por id{Cores.FIM}")
    print(f"{Cores.TEXTO}4 - Deletar rotulo por id{Cores.FIM}")
    print('*' * 30)
    print(f"{Cores.AVISO}0 - SAIR{Cores.FIM}")
    print('*' * 30)
    opcao_sub = int(input(f"{Cores.INPUT}Digite a opção: {Cores.FIM}"))
    clear()

    if opcao_sub == 1:
      exibir_rotulo(conn)
    if opcao_sub == 2:
      inserir_rotulo(conn)
    if opcao_sub == 3:
      atualizar_rotulo(conn)
    if opcao_sub == 4:
      deletar_rotulo(conn)

    input(f"\n{Cores.INPUT}Pressione <ENTER> para continuar ...{Cores.FIM}")
    clear()
