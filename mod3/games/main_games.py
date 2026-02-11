from games.list_games import menu_game_list
from util.menu import game_menu
from util.validator import validateInput
from util.utils import clear_screen, generate_game_id, find_element
from data.data_access import add_game, del_game, get_game_by_id, get_categories, get_games
import time

def menu_games():
  while True:
    clear_screen()
    n_opt = 4
    print(game_menu)
    option = input('Ingrese una opcion.. ')

    if validateInput(option, n_opt):
      match (option):
        case '1':
          add_game_screen()
          continue 
        case '2':
          del_game_screen()
          continue
        case '3':
          menu_game_list()
          continue
        case '4':
          print('Volver al menu principal')
          break
    else:
      input('Presione una tecla para continuar.')

def add_game_screen():
  try:
    while True:
      clear_screen()
      print("""
      ######################
      #   INGRESAR JUEGO   #
      ######################
      Presione Ctrl+C para cancelar.
      """)
      name = input('Ingrese nombre del juego: ')
      
      if not name:
        print('Debe ingresar el nombre del juego.')
        input('Presione una tecla para continuar..')
        continue

      name = name.title()
      description = input('Ingrese descripcion del juego: ')

      cat_list = get_categories()[1:]
      cat_names = [c['name'] for c in cat_list]
      print('\nCategorias: ', *cat_names, '\n', sep=' | ')      
      categorias = input('Ingrese categorias (separadas por espacio): ')
      categorias = categorias.lower().split()
      categorias = [c['id'] for c in cat_list if c['name'] in categorias]

      if not categorias:
        categorias = [0]

      game = {
        "id": generate_game_id(),
        "name": name,
        "description": description,
        "minutes": 0,
        "completion": 0,
        "categories": categorias
      }
      add_game(game)
      break
  except KeyboardInterrupt:
    print("\nSe ha cancelado la operacion.")
    time.sleep(1.5)

def del_game_screen():
  try:
    while True:
      clear_screen()
      print("""
      ######################
      #   ELIMINAR JUEGO   #
      ######################
      Presione Ctrl+C para cancelar.
      """)

      games = get_games()

      if not games:
        print('No existen juegos en el sistema.')
        time.sleep(1.5)
        continue
      else:
        for g in games:
          print(f'id: {g['id']} - Nombre: {g['name']}')
          
      game_id = input('\nIngrese id del juego: ')

      if not game_id or not game_id.isdigit():
        print('Debe ingresar id de juego valido.')
        input('Presione una tecla para continuar..')
        continue

      game_id = int(game_id)
      
      if get_game_by_id(game_id):  
        del_game(game_id)
        break
      else:
        print('Id de juego no encontrado.')
        input('Presione una tecla para continuar..')
        continue
  except KeyboardInterrupt:
    print("\nSe ha cancelado la operacion.")
    time.sleep(1.5)