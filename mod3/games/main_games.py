from util.menu import game_menu
from games.list_games import menu_game_list
from util.validator import validateInput
import os

def menu_games():
  while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    n_opt = 4
    print(game_menu)
    option = input('Ingrese una opcion.. ')

    if validateInput(option, n_opt):
      match (option):
        case '1':
          print('Agregar juego')
          input()
          continue 
        case '2':
          print('Eliminar juego')
          input()
          continue
        case '3':
          menu_game_list()
          continue
        case '4':
          print('Volver al menu principal')
          break
    else:
      input('Presione una tecla para continuar.')