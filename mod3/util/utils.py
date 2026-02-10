import os, random

game_id_range = 1000

def find_element(key, key_value, datalist):
  """
  Busca un elemento en una lista a partir de una llave y un valor dados.
  Args:
    key (str): Llave que indica el campo que se desea evaluar.
    key_value (any): Valor que se busca para la llave ingresada.
    datalist (list): Lista en la que se busca el valor dado.
  Returns:
    any, bool: El item buscado o False si no se encuentra.
  """
  found_item = next((i for i in datalist if i[key] == key_value), None)
  return found_item if found_item else False
  
def filter_col(key, key_value, datalist):
  """
  Filtra uno o mas elementos de una lista.
  Args:
    key (str): Llave que indica el campo a comparar.
    key_value (any): Valor que indica el criterio del filtro.
    datalist: Lista que contiene los elementos a evaluar.
  Returns:
    list(any): Lista que retorna los elementos no coincidentes con la Llave-Valor.
  """
  iter = filter(lambda c: c[key] != key_value, datalist)
  return list(iter)

def order_json(datalist, keys):
  """
  Ordena una lista correspondiente a la data de un archivo JSON.
  Args:
    datalist (list): Lista que representa los datos de un archivo JSON.
    keys (list): Lista que contiene las llaves para ordenar la lista JSON.
  Returns:
    list(any): Lista ordenada a partir de las llaves ingresadas.
  """
  return sorted(datalist, key=lambda x: set_keys(x, keys))

def set_keys(x, keys):
  """
  Genera una tupla con los campos que indican el criterio de orden de la lista.
  Args:
    x (any): Elemento de una lista al que se aplicara el orden.
    keys (list): Llaves asociadas un elemento de una lista.
  Returns:
    tupla: Tupla que contiene elementos de tipo elemento[key]. (x[key])
  """
  k_lst = []
  for key in keys:
    k_lst.append(x[key])
  return tuple(k_lst)

def generate_game_id():
  """
  Genera un id aleatorio entre 1 y el rango maximo definido.
  Returns:
    int: id generado aleatoriamente.
  """
  return random.randint(1, game_id_range + 1);

def clear_screen():
  """ Limpia la pantalla de la consola. """
  os.system('cls' if os.name == 'nt' else 'clear')