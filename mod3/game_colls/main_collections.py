from util.menu import coleccion_menu
from util.validator import validateInput
import os

def menu_collections():
  while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    n_opt = 5
    print(coleccion_menu)
    option = input('Ingrese una opcion.. ')

    if validateInput(option, n_opt):
      match (option):
        case '1':
          print('Agregar Juego a coleccion')
          input()
          continue
        case '2':
          print('Agregar coleccion')
          input()
          continue 
        case '3':
          print('Eliminar coleccion')
          input()
          continue
        case '4':
          print('Listar colecciones')
          input()
          continue
        case '5':
          print('Volver al menu principal')
          break
    else:
      input('Presione una tecla para continuar.')