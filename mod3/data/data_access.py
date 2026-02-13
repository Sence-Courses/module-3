import json
from util.utils import order_datalist, filter_col, find_element, get_list_by_match
from util.enums import OrderKeys
import time

default_path = 'mod3/data/'

def add_game(game):
  """
  Agrega un juego al sistema.
  Args:
    game (dict): Objeto que contiene los datos de un juego.
  """
  coll_id = 'game_def'
  games = read_json(coll_id)
  games.append(game)
  write_json(coll_id, games)
  input(f'\nEl juego {game["name"]} se ha agregado.\nPresione una tecla para continuar.')

def get_game_by_id(game_id):
  """
  Retorna un juego guardado en el sistema a traves de su id.
  Args:
    game_id (int): Id del juego a buscar.
  Returns:
    any, bool: El item buscado o False si no se encuentra.
  """
  coll_id = 'game_def'
  games = read_json(coll_id)
  return find_element('id', game_id, games)

def get_gamelist_by_name(name):
  """
  Obtiene una lista de juegos a partir de un nombre.
  Args:
    name (str): Nombre o fragmento del nombre del juego.
  Returns:
    list: Retorna una lista de juegos o una lista vacia.
  """
  coll_id = 'game_def'
  key = 'name'
  games = read_json(coll_id)
  return get_list_by_match(key, name, games)

def get_ordered_gamelist(origin, reverse):
  """
  Retorna una lista de juegos ordenada a partir de las opciones ingresadas.
  Args:
    origin (str): Indicador para identificar los campos a ordenar.
    reverse (bool): Indica si el orden sera ascendente o descendente.
  Returns:
    list: Retorna la lista de juegos ordenada por los campos solicitados.
  """
  coll_id = 'game_def'
  game_list = read_json(coll_id)

  match (origin):
    case 'by_hours':
      game_list = order_datalist(
        game_list, OrderKeys['game_hrs'].value, reverse)
    case 'by_compl':
      game_list = order_datalist(
        game_list, OrderKeys['game_cmp'].value, reverse)
  return game_list;

def get_gamelist_by_category(category):
  """
  Retorna una lista de juegos a partir de su categoria.
  Args:
    category (int): Id de la categoria a buscar.
  Returns:
    list: Retorna una lista de juegos o una lista vacia.
  """
  coll_id = 'game_def'
  key = 'categories'
  games = read_json(coll_id)
  return get_list_by_match(key, category, games)

def del_game(game_id):
  """
  Elimina un juego del sistema apartir de su id.
  Args:
    game_id (int): Id del juego a eliminar.
  """
  coll_id = 'game_def'
  games = read_json(coll_id)
  game = get_game_by_id(game_id)
  games = filter_col('id', game_id, games)
  write_json(coll_id, games)
  input(f'\nEl juego {game["name"]} ha sido eliminado.\nPresione una tecla para continuar.')

def get_games():
  """
  Retorna una lista con los juegos guardados en el sistema.
  Returns:
    list: Lista de juegos guardados en el sistema.
  """
  coll_id = 'game_def'
  return read_json(coll_id)

def get_categories():
  """
  Obtiene las categorias que pueden ser aplicadas a los juegos.
  Returns:
    list: Lista con las categorias de juegos del sistema. No incluye la primera opcion.
  """
  col_id = 'categories'
  categories = read_json(col_id)
  return categories

def get_name_categories_by_id(cat_ids):
  """
  Retorna una lista de nombres de categorias a partir de ids.
  """
  key = 'categories'
  categories = get_categories()
  filtered_categories = list(filter(lambda c: c['id'] in cat_ids, categories))
  cat_names = list(map(lambda c: c['name'], filtered_categories))
  return cat_names

def get_category_by_name(category):
  col_id = 'categories'
  key = 'name'
  categories = read_json(col_id)
  return get_list_by_match(key, category.lower(), categories)

def write_json(col_name, json_data):
  """
  Graba el contenido de una lista en un archivo JSON.
  Args:
    col_name (str): Nombre del archivo JSON.
    json_data (list): Lista que contiene los datos a guardar.
  """
  try:
    filename = default_path + col_name + '.json'
    with open(filename, 'w') as json_file:
      json.dump(order_datalist(json_data, OrderKeys[col_name].value), json_file, indent=2)
  except IOError as e:
    print(f"Error al guardar la data: {e}")
  except TypeError as e:
    print(f"Error al serializar la data: {e}")

def read_json(col_name):
  """
  Retorna una lista con el contenido de un archivo JSON.
  Args:
    col_name (str): Nombre del archivo JSON.
  Returns:
    list: Lista que contiene el contenido de un archivo JSON.
  """
  filename = default_path + col_name + '.json'
  try:
    with open(filename, 'r') as json_file:
      return json.load(json_file)
  except FileNotFoundError:
    print(f"Error: Archivo '{json_file}' no encontrado.")
  except json.JSONDecodeError:
    print("Error: Error al decodificar el archivo JSON. Revise la sintaxis del archivo.")