from games.main_games import menu_games
from game_colls.main_collections import menu_collections
from history.main_history import menu_history
from util.menu import main_menu
from util.validator import validateInput
from util.utils import clear_screen

def main():
  while True:
    clear_screen()
    n_opt = 5
    print(main_menu)
    option = input('Ingrese una opcion.. ')

    if validateInput(option, n_opt):
      match (option):
        case '1':
          menu_games()
          continue 
        case '2':
          menu_collections()
          continue
        case '3':
          menu_history()
          continue
        case '4':
          print('Simular juego')
          input()
          continue
        case '5':
          print('Salir')
          break
    else:
        input('Presione una tecla para continuar.')

if __name__ == "__main__":
  main()