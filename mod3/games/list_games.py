from util.menu import list_games_menu
from util.validator import validateInput
import os

def menu_game_list():
  while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    n_opt = 6
    print(list_games_menu)
    option = input('Ingrese una opcion.. ')

    if validateInput(option, n_opt):
      match (option):
        case '1':
          print('Buscar por nombre')
          input()
          continue
        case '2':
          print('Buscar por coleccion')
          input()
          continue 
        case '3':
          print('Buscar por categoria')
          input()
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