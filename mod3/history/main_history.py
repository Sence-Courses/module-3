import time
from util.menu import history_menu
from util.validator import validateInput
from util.utils import clear_screen
from data.data_access import get_game_history
import os, time

def menu_history():
  while True:
    clear_screen()
    n_opt = 3
    print(history_menu)
    option = input('Ingrese una opcion.. ')

    if validateInput(option, n_opt):
      match (option):
        case '1':
          print('Historial de juegos')
          game_history()
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

def game_history():
  try:
    while True:
      clear_screen()
      print(
      """
      #######################
      # HISTORIAL DE JUEGOS #
      #######################
      Presione Ctrl+C para salir.
      """)
      historial = get_game_history()
      for register in historial:
        print(register)
      input('\nPresione una tecla para continuar...')
  except KeyboardInterrupt:
    print("\nVolviendo la menu anterior.")
    time.sleep(1.5)