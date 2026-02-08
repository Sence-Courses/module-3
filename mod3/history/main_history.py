from util.menu import history_menu
from util.validator import validateInput
import os

def menu_history():
  while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    n_opt = 3
    print(history_menu)
    option = input('Ingrese una opcion.. ')

    if validateInput(option, n_opt):
      match (option):
        case '1':
          print('Historial de juegos')
          input()
          continue 
        case '2':
          print('Historial de colecciones')
          input()
          continue
        case '3':
          print('Volver al menu principal')
          break
    else:
      input('Presione una tecla para continuar.')