from util.menu import list_games_menu
from util.validator import validateInput
from data.data_access import get_categories, get_category_by_name, get_gamelist_by_name, get_gamelist_by_category, get_name_categories_by_id
from util.utils import clear_screen
import os, time

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
          print('Listar por horas jugadas')
          input()
          continue
        case '5':
          print('Listar por % completado')
          input()
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