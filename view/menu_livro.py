from model.livro import Livro
from terminal_clear import clear
import matplotlib.pyplot as graficoLivro
from cores import Cores


def exibir_livro(conn):
  values = Livro.get_livro(conn)
  if values != []:
    for i in range(len(values)):
      lido = "Sim" if values[i][2] == 1 else "Não"
      print(f"{Cores.TEXTO}ID: {Cores.FIM} {values[i][0]}")
      print(f"{Cores.TEXTO}Nome: {Cores.FIM} {values[i][1]}")
      print(f"{Cores.TEXTO}Lido: {Cores.FIM} {lido}\n\n")
  else:
    print(f"\n{Cores.AVISO}Não existe livros cadastrados!!!{Cores.FIM}")


def exibir_rotulo_livro(conn):
  values = Livro.exibir_rotulo_livro(conn)
  if values != []:
    for i in range(len(values)):
      lido = "Sim" if values[i][2] == 1 else "Não"
      print(f"{Cores.TEXTO}ID: {Cores.FIM} {values[i][0]}")
      print(f"{Cores.TEXTO}Nome: {Cores.FIM} {values[i][1]}")
      print(f"{Cores.TEXTO}Lido: {Cores.FIM} {lido}")
      print(f"{Cores.TEXTO}ID do rotulo: {Cores.FIM} {values[i][3]} ")
      print(f"{Cores.TEXTO}Nº Pags: {Cores.FIM} {values[i][4]} ")
      print(f"{Cores.TEXTO}Preco: {Cores.FIM} {values[i][5]} ")
      print(f"{Cores.TEXTO}Categoria: {Cores.FIM} {values[i][6]} ")
      print(f"{Cores.TEXTO}Sinopse: {Cores.FIM} {values[i][7]} ")
      print(f"{Cores.TEXTO}Autor: {Cores.FIM} {values[i][8]} ")
      print(f"{Cores.TEXTO}Ano: {Cores.FIM} {values[i][9]} \n\n")
  else:
    print(f"\n{Cores.AVISO}Não existe livros cadastrados!!!{Cores.FIM}")


def inserir_livro(conn):

  nomeLivro = input("Escreva o nome do livro: ")
  lido = input("Esse livro já foi lido? \n 1 - Sim \n 0 - Não ")
  while lido < '0' or lido > '1':
    print("Valor inválido!!!\n")
    lido = input("Esse livro já foi lido? \n 1 - Sim \n 0 - Não ")

  livro = Livro(nomeLivro, lido)
  result = livro.add_livro(conn)
  if result != None:
    print(result)
  else:
    print(f"\n{Cores.SUCESSO}Livro inserido com sucesso!!!{Cores.FIM}")


def atualizar_livro(conn):
  id = input("Digite o ID do livro que você quer atualizar: ")
  nomeLivro = input("Digite um novo nome para o livro: ")
  lido = int(input("Esse livro já foi lido? \n 1 - Sim \n 0 - Não "))
  while lido < 0 or lido > 1:
    print("Valor inválido!!!")
    lido = input("Ele já foi lido? 1 - para sim 0 - para não")
  values = (nomeLivro, lido, id)
  result = Livro.update_livro(conn, values)
  if result != None:
    print(result)
  else:
    print(f"\n{Cores.SUCESSO}Livro atualizado com sucesso!!!{Cores.FIM}")


def deletar_livro(conn):
  id = (input("Digite o ID do rotulo que deseja deletar: "), )
  result = Livro.deletar_livro(conn, id)
  if result != None:
    print(result)
  else:
    print(f"\n{Cores.SUCESSO}Livro deletado com sucesso!!!{Cores.FIM}")


def atualizar_lido_livro(conn):
  id = input("Digite o ID do livro que você quer marcar como lido:")
  lido = input(
    "Você quer atualizar para qual status de leitura? \n 1 - Lido \n 0 - Não lido"
  )
  while lido < '0' or lido > '1':
    print("Valor inválido!!!")
    lido = input(
      "Você quer atualizar para qual status de leitura? 1 - para sim 0 - para não"
    )
  result = Livro.lido_livro(conn, id, lido)
  if result != None:
    print(result)
  else:
    print(f"\n{Cores.SUCESSO}Livro atualizado com sucesso!!!{Cores.FIM}")


def gerar_grafico_livro(conn):
  result = Livro.grafico_categoria_livro(conn)
  categorias = result[0]
  contagemCategorias = result[1]
  graficoLivro.xlabel("Categorias")
  graficoLivro.ylabel("Número de Livros")
  '''graficoLivro.plot(categorias, contagemCategorias)
  graficoLivro.show()'''
  graficoLivro.plot(categorias, contagemCategorias)
  graficoLivro.show(block=False)


#submenu
def submenu(conn):
  opcao_sub = None
  while opcao_sub != 0:
    print('*' * 30)
    print(f"{Cores.TEXTO}1 - Exibir todos os livros{Cores.FIM}")
    print(f"{Cores.TEXTO}2 - Exibir livros com rótulos{Cores.FIM}")
    print(f"{Cores.TEXTO}3 - Cadastrar um livro{Cores.FIM}")
    print(f"{Cores.TEXTO}4 - Atualizar um livro{Cores.FIM}")
    print(f"{Cores.TEXTO}5 - Deletar um livro{Cores.FIM}")
    print(
      f"{Cores.TEXTO}6 - Definir um livro como lido ou não lido{Cores.FIM}")
    print(f"{Cores.TEXTO}7 - Grafíco Número de livros{Cores.FIM}")
    print('*' * 30)
    print(f"{Cores.AVISO}0 - SAIR{Cores.FIM}")
    print('*' * 30)
    opcao_sub = int(input(f"{Cores.INPUT}Digite a opção: {Cores.FIM}"))
    clear()

    if opcao_sub == 1:
      exibir_livro(conn)

    if opcao_sub == 2:
      exibir_rotulo_livro(conn)

    if opcao_sub == 3:
      inserir_livro(conn)

    if opcao_sub == 4:
      atualizar_livro(conn)

    if opcao_sub == 5:
      deletar_livro(conn)

    if opcao_sub == 6:
      atualizar_lido_livro(conn)

    if opcao_sub == 7:
      gerar_grafico_livro(conn)

    input(f"\n{Cores.INPUT}Pressione <ENTER> para continuar ...{Cores.FIM}")
    clear()
