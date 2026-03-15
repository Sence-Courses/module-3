import time
from util.menu import list_games_menu
from util.validator import validateInput
from data.data_access import (
  get_categories, 
  get_category_by_name, 
  get_gamelist_by_name, 
  get_gamelist_by_category, 
  get_name_categories_by_id,
  get_ordered_gamelist)
from util.utils import clear_screen, get_formatted_time

def menu_game_list():
  while True:
    clear_screen()
    n_opt = 6
    print(list_games_menu)
    option = input('Ingrese una opcion.. ')

    if validateInput(option, n_opt):
      match (option):
        case '1':
          find_By_name()
          continue
        case '2':
          print('Buscar por coleccion')
          input()
          continue 
        case '3':
          find_by_category()
          continue
        case '4':
          list_by_hours()
          continue
        case '5':
          list_by_completion()
          continue
        case '6':
          print('Volver al menu anterior')
          break
    else:
      input('Presione una tecla para continuar.')

def find_By_name():
  try:
    while True:
      clear_screen()
      print(
      """
      #################################
      # BUSQUEDA DE JUEGOS POR NOMBRE #
      #################################
      Presione Ctrl+C para salir.
      """)
      name = input('\nIngrese el nombre del juego a buscar: ')

      if not name:
        print('\nDebe ingresar un nombre o parte de este.')
        continue

      game_list = get_gamelist_by_name(name.title())

      if not game_list:
        print(f'\nNo se encontraron juegos con el nombre {name}.')
        input('\nPresione una tecla para continuar...')
        continue

      for g in game_list:
        print(f'\nJuego: {g['name']}')
        print(f'Descripcion: {g['description']}')
        cat_names = get_name_categories_by_id(g['categories'])
        print('Categorias: ',*cat_names)
      
      input('\nPresione una tecla para continuar...')
  except KeyboardInterrupt:
    print("\nVolviendo la menu anterior.")
    time.sleep(1.5)

def find_by_category():
  try:
    while True:
      clear_screen()
      print(
      """
      ####################################
      # BUSQUEDA DE JUEGOS POR CATEGORIA #
      ####################################
      Presione Ctrl+C para salir.
      """)

      cat_list = get_categories()[1:]
      cat_names = [c['name'] for c in cat_list]
      print('\nCategorias: ', *cat_names, '\n', sep=' | ')

      category = input('\nIngrese la categoria de juegos a buscar: ')

      if not category:
        print('\nDebe ingresar una categoria.')
        input('Presione una tecla para continuar..')
        continue

      found_category = get_category_by_name(category)

      if not found_category:
        print(f'La categoria {category} no existe.')
        input('Presione una tecla para continuar..')
        continue

      game_list = get_gamelist_by_category(found_category[0]['id'])

      if not game_list:
        print(f'\nNo se encontraron juegos con la categoria {category}.')
        input('Presione una tecla para continuar..')
        continue

      for g in game_list:
        print(f'\nJuego: {g['name']}')
        print(f'Descripcion: {g['description']}')
        cat_names = get_name_categories_by_id(g['categories'])
        print('Categorias: ',*cat_names)
      
      input('\nPresione una tecla para continuar...')
  except KeyboardInterrupt:
    print("\nVolviendo la menu anterior.")
    time.sleep(1.5)

def list_by_hours():
  try:
    while True:
      clear_screen()
      n_opt = 2
      print(
      """
      ############################# 
      # LISTADO POR HORAS JUGADAS #
      #############################
      Presione Ctrl+C para salir.
      """)
      order = input("""
      1. Orden ascendente.
      2. Orden descendente.
      """)

      if validateInput(order, n_opt):
        game_list = []
        origin = 'by_hours'

        match (order):
          case '1':
            game_list = get_ordered_gamelist(origin, False)
          case '2':
            game_list = get_ordered_gamelist(origin, True)

        for g in game_list:
          print(f'\nJuego: {g['name']}')
          print(f'Descripcion: {g['description']}')
          cat_names = get_name_categories_by_id(g['categories'])
          print('Categorias: ', *cat_names)
          print(f'Horas jugadas: {get_formatted_time(g['minutes'])}')

        input('\nPresione una tecla para continuar...')
      else:
        input('Presione una tecla para continuar.')
  except KeyboardInterrupt:
    print("\nVolviendo la menu anterior.")
    time.sleep(1.5)

def list_by_completion():
  try:
    while True:
      clear_screen()
      n_opt = 2
      print(
      """
      ########################## 
      #   LISTADO POR AVANCE   #
      ##########################
      Presione Ctrl+C para salir.
      """)
      order = input("""
      1. Orden ascendente.
      2. Orden descendente.
      """)

      if validateInput(order, n_opt):
        game_list = []
        origin = 'by_compl'

        match (order):
          case '1':
            game_list = get_ordered_gamelist(origin, False)
          case '2':
            game_list = get_ordered_gamelist(origin, True)

        for g in game_list:
          print(f'\nJuego: {g['name']}')
          print(f'Descripcion: {g['description']}')
          cat_names = get_name_categories_by_id(g['categories'])
          print('Categorias: ', *cat_names)
          print(f'completion completado: {g['completion']}%')

        input('\nPresione una tecla para continuar...')
      else:
        input('Presione una tecla para continuar.')
  except KeyboardInterrupt:
    print("\nVolviendo la menu anterior.")
    time.sleep(1.5)